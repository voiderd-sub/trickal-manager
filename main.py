from PySide6 import QtWidgets
from PySide6.QtCore import QEvent

from PySide6.QtWidgets import QMessageBox
from PySide6.QtGui import QIcon

from widgets.ui.main_window import Ui_MainWindow
from widgets.wrapper.account_settings import AccountSettings
from widgets.wrapper.goal_settings import GoalSettings
from widgets.wrapper.resource_manager import ResourceManager

from functools import partial
import sqlite3, yaml, os.path
import requests
from zipfile import ZipFile
from io import BytesIO
from pathlib import Path


"""
!WARNING!
If you converted the .ui file to a .py file with the pyside6-uic command,
you must pass "self.stacked_widget" as an argument to each custom widget
constructor of stackedwindow in main_window.py.
"""

BRANCH = "feature_autoupdate"

def downloadIcons():
    # URL of the zip file on GitHub
    branch = BRANCH
    zip_url = f"https://github.com/voiderd-sub/trickcal-manager/raw/{branch}/icon.zip"
    
    # Local file paths
    response = requests.get(zip_url)
    response.raise_for_status()

    with ZipFile(BytesIO(response.content)) as zip_ref:
        zip_ref.extractall(".")


def download_file(url, destination_path):
    # destination_path must be a file
    destination_path = Path(destination_path)
    assert destination_path.is_file() or not destination_path.exists()
    os.makedirs(destination_path.parent, exist_ok=True)

    # Download a file from a URL
    response = requests.get(url)
    response.raise_for_status()
    
    with open(destination_path, 'wb') as file:
        file.write(response.content)



class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        # open db & config
        self.configInit()
        self.masterDBInit()
        self.userDBInit()
        self.resource = ResourceManager(self)

        # generate subwindows
        self.account_settings = AccountSettings(parent=self)
        self.goal_settings = GoalSettings(parent=self)

        self.setupUi(self)
        self.setInitialState()
        self.stacked_window.setCurrentIndex(0)

    
    def setInitialState(self):
        # Connect btns with pages with each page
        for i, name in enumerate(self.sidebar.btn_with_pages):
            btn=getattr(self.sidebar, name)
            btn.clicked.connect(partial(self.stacked_window.setCurrentIndex, i))


    def closeEvent(self, event):
        self.conn_master.close()
        self.conn_user.close()
        with open('db/config.yaml', 'w') as f:
            yaml.dump(self.config, f)
        event.accept()


    def masterDBInit(self, force=False):
        if hasattr(self, "conn_master"):
            self.conn_master.close()
              
        db_path = "db/master.db"
        if force or not os.path.isfile(db_path):
            self.downloadMasterDB()
        self.conn_master = sqlite3.connect(db_path)


    def downloadMasterDB(self):
        try:
            user_name = "voiderd-sub"
            repository = "trickal-manager"
            branch = BRANCH
            destination_path = "db/master.db"
            url = f"https://github.com/{user_name}/{repository}/raw/{branch}/db/master.db"
            download_file(url, destination_path)
            downloadIcons()

        except Exception as e:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setWindowTitle("Error")
            msg_box.setText(str(e))
            msg_box.exec()
            raise e
        


    def userDBInit(self):
        user_name = self.config["account_list"][self.config["cur_account_idx"]]
        db_path = f"db/{user_name}.db"

        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.executescript(
"""
CREATE TABLE IF NOT EXISTS "user_hero" (						-- 유저가 보유한 사도 리스트 (table에 있으면 보유중)
	"hero_id"	INTEGER,						-- 사도 id
	"star_extrinsic"	INTEGER NOT NULL,		-- 현재 별 개수
	PRIMARY KEY("hero_id")
);
CREATE TABLE IF NOT EXISTS "user_cur_equip" (                 -- 유저의 현재 장비 장착 상태
    "hero_id"	INTEGER NOT NULL,               -- 사도 id
    "rank"	INTEGER NOT NULL,                   -- 사도의 현재 랭크
    "equips"	TEXT,                           -- 장착한 장비 order값
    PRIMARY KEY("hero_id")
);
CREATE TABLE IF NOT EXISTS "user_goal_equip_names" (          -- 유저가 설정한 목표 이름
    "id"	INTEGER PRIMARY KEY,
    "name"	TEXT NOT NULL UNIQUE
);
CREATE TABLE IF NOT EXISTS "user_goal_equip" (                -- 유저가 설정한 목표 상세 내역
    "goal_id"	INTEGER NOT NULL,               -- 목표 id
    "hero_id"	INTEGER NOT NULL,               -- 사도 id
    "rank"	INTEGER NOT NULL,                   -- 목표 랭크
    "equips"	TEXT,                           -- 목표 장비 order값
    PRIMARY KEY("goal_id","hero_id")
);
CREATE TABLE IF NOT EXISTS "user_items" (       -- 유저가 보유한 재료 리스트
    "name"    TEXT NOT NULL UNIQUE,             -- 재료 이름
    "count"    INTEGER NOT NULL,                -- 재료 개수
    PRIMARY KEY("name")
);
CREATE TABLE IF NOT EXISTS "user_bag_equips"(   -- 유저가 보유한 장비 리스트
    "id"    INTEGER NOT NULL,                   -- 장비 id
    "count"    INTEGER NOT NULL,                -- 장비 개수
    PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "calc_settings" (    -- 계산 설정
    "setting_name"    TEXT NOT NULL UNIQUE,     -- 설정 이름
    "value"    INTEGER NOT NULL,                   -- 설정 값
    PRIMARY KEY("setting_name")
);
PRAGMA journal_mode=wal;
""")
        cur.execute("SELECT count(_rowid_) FROM user_goal_equip_names")
        if cur.fetchone()[0] == 0:
            cur.execute("""INSERT INTO "user_goal_equip_names" (id, name) VALUES (1, '기본 목표');""")
        
        master_cur = self.conn_master.cursor()
        master_cur.execute("""
SELECT t.comment ||" "||CASE WHEN i.piece_recipe = 1 THEN "조각" ELSE "도안" END || "("||i.rank||"티어)" as name
FROM items i
join item_type t on (i.type = t.type_id)
""")
        cur.executemany("INSERT OR IGNORE INTO user_items VALUES (?,?)", [(*i, 0) for i in master_cur])

        # TODO: check user_version and add/modify columns

        conn.commit()
        conn.close()
        self.conn_user = sqlite3.connect(db_path)


    def configInit(self):
        config_path = "db/config.yaml"
        if not os.path.isfile(config_path):
            with open(config_path, "w") as f:
                f.write(
"""
account_list:
    - user 1
cur_account_idx: 0
path_item_table: 1hntR5RyQ7UDXwfnEdjIu9Of369O_68FYRjIleBpdn7w
""")
        
        with open("db/config.yaml") as f:
            self.config = yaml.load(f, Loader=yaml.FullLoader)
    
    def updateAccountList(self):
        self.sidebar.updateLocalAccountList(True)

    def updateGoalList(self):
        self.resource.delete("GoalList")
        self.page_equip_1.updateGoalNameList()
        self.page_equip_3.updateGoalList()

    def changeAccountCascade(self):
        self.userDBInit()
        self.resource.deleteAll(user=True)
        self.page_hero.updateTable()
        self.page_equip_1.changeAccount()
        self.page_equip_2.reloadData()
        self.page_equip_3.updateGoalList()
    
    def changeExtrinsicStarsCascade(self):
        self.resource.delete("HeroIdToStarExtrinsic")
    
    def masterDBUpdateCascade(self):
        self.masterDBInit(force=True)
        self.resource.deleteAll(master=True)
        self.resource.masterInit()
        self.page_hero.constructTable()
        self.page_equip_1.updateHeroList()
        self.page_equip_2.loadMaterialTableColumns()
        self.page_equip_2.reloadData()
        
        # TODO : update hero list of page_crayon_1


if __name__ == "__main__":
    # os.chdir("_internal")

    # Check whether icon folder exists
    if os.path.isdir("icon") == False:
        downloadIcons()

    app = QtWidgets.QApplication([])
    app.setWindowIcon(QIcon('icon/icon.png'))

    window = MainWindow()
    window.show()

    app.exec()