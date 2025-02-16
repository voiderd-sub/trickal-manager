# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_equip_2.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

from widgets.wrapper.misc import MaterialTableWidget

class Ui_page_equip_2(object):
    def setupUi(self, page_equip_2):
        if not page_equip_2.objectName():
            page_equip_2.setObjectName(u"page_equip_2")
        page_equip_2.resize(800, 600)
        self.verticalLayout_3 = QVBoxLayout(page_equip_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(15, 20, 15, 20)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.widget = QWidget(page_equip_2)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"ONE Mobile POP"])
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.material_table = MaterialTableWidget(self.widget)
        self.material_table.setObjectName(u"material_table")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.material_table.sizePolicy().hasHeightForWidth())
        self.material_table.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamilies([u"ONE Mobile POP"])
        font1.setPointSize(12)
        self.material_table.setFont(font1)

        self.verticalLayout.addWidget(self.material_table)

        self.verticalSpacer_5 = QSpacerItem(20, 34, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_5)


        self.horizontalLayout_3.addWidget(self.widget)

        self.widget_2 = QWidget(page_equip_2)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy2)
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_6)

        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.bag_equip_table = QTableWidget(self.widget_2)
        self.bag_equip_table.setObjectName(u"bag_equip_table")
        self.bag_equip_table.setFont(font1)

        self.verticalLayout_2.addWidget(self.bag_equip_table)

        self.verticalSpacer_7 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_7)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_4 = QSpacerItem(40, 23, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.add_btn = QPushButton(self.widget_2)
        self.add_btn.setObjectName(u"add_btn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.add_btn.sizePolicy().hasHeightForWidth())
        self.add_btn.setSizePolicy(sizePolicy3)
        self.add_btn.setMinimumSize(QSize(120, 0))
        font2 = QFont()
        font2.setFamilies([u"ONE Mobile POP"])
        font2.setPointSize(14)
        self.add_btn.setFont(font2)

        self.horizontalLayout_2.addWidget(self.add_btn)

        self.delete_btn = QPushButton(self.widget_2)
        self.delete_btn.setObjectName(u"delete_btn")
        sizePolicy3.setHeightForWidth(self.delete_btn.sizePolicy().hasHeightForWidth())
        self.delete_btn.setSizePolicy(sizePolicy3)
        self.delete_btn.setMinimumSize(QSize(120, 0))
        self.delete_btn.setFont(font2)

        self.horizontalLayout_2.addWidget(self.delete_btn)

        self.horizontalSpacer_5 = QSpacerItem(37, 23, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_3.addWidget(self.widget_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.retranslateUi(page_equip_2)

        QMetaObject.connectSlotsByName(page_equip_2)
    # setupUi

    def retranslateUi(self, page_equip_2):
        page_equip_2.setWindowTitle(QCoreApplication.translate("page_equip_2", u"Form", None))
        self.label.setText(QCoreApplication.translate("page_equip_2", u"\ubcf4\uc720 \ub3c4\uc548 / \uc870\uac01", None))
        self.label_2.setText(QCoreApplication.translate("page_equip_2", u"\ubcf4\uc720 \uc644\uc81c\ud488", None))
        self.add_btn.setText(QCoreApplication.translate("page_equip_2", u"\ucd94\uac00", None))
        self.delete_btn.setText(QCoreApplication.translate("page_equip_2", u"\uc0ad\uc81c", None))
    # retranslateUi

