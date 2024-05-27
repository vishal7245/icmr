# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'breakpoint_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QHBoxLayout,
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1080, 720)
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 680, 221, 26))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.breakpoint_add_button = QPushButton(self.layoutWidget)
        self.breakpoint_add_button.setObjectName(u"breakpoint_add_button")

        self.horizontalLayout_2.addWidget(self.breakpoint_add_button)

        self.breakpoint_delete_button = QPushButton(self.layoutWidget)
        self.breakpoint_delete_button.setObjectName(u"breakpoint_delete_button")

        self.horizontalLayout_2.addWidget(self.breakpoint_delete_button)

        self.breakpoint_table = QTableWidget(Dialog)
        self.breakpoint_table.setObjectName(u"breakpoint_table")
        self.breakpoint_table.setGeometry(QRect(20, 140, 1041, 521))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 891, 16))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 30, 741, 16))
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 50, 751, 16))
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 90, 131, 16))
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(290, 90, 131, 16))
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(490, 90, 131, 16))
        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(710, 90, 131, 16))
        self.label_8 = QLabel(Dialog)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(890, 90, 131, 16))
        self.layoutWidget1 = QWidget(Dialog)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(840, 680, 221, 26))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.breakpoint_ok_button = QPushButton(self.layoutWidget1)
        self.breakpoint_ok_button.setObjectName(u"breakpoint_ok_button")

        self.horizontalLayout.addWidget(self.breakpoint_ok_button)

        self.breakpoint_cancel_button = QPushButton(self.layoutWidget1)
        self.breakpoint_cancel_button.setObjectName(u"breakpoint_cancel_button")

        self.horizontalLayout.addWidget(self.breakpoint_cancel_button)

        self.breakpoint_organism_combobox = QComboBox(Dialog)
        self.breakpoint_organism_combobox.setObjectName(u"breakpoint_organism_combobox")
        self.breakpoint_organism_combobox.setGeometry(QRect(20, 110, 261, 24))
        self.breakpoint_siteofinfection_combobox = QComboBox(Dialog)
        self.breakpoint_siteofinfection_combobox.setObjectName(u"breakpoint_siteofinfection_combobox")
        self.breakpoint_siteofinfection_combobox.setGeometry(QRect(290, 110, 191, 24))
        self.breakpoint_antibiotic_combobox = QComboBox(Dialog)
        self.breakpoint_antibiotic_combobox.setObjectName(u"breakpoint_antibiotic_combobox")
        self.breakpoint_antibiotic_combobox.setGeometry(QRect(490, 110, 211, 24))
        self.breakpoint_testmethod_combobox = QComboBox(Dialog)
        self.breakpoint_testmethod_combobox.setObjectName(u"breakpoint_testmethod_combobox")
        self.breakpoint_testmethod_combobox.setGeometry(QRect(710, 110, 171, 24))
        self.breakpoint_type_combobox = QComboBox(Dialog)
        self.breakpoint_type_combobox.setObjectName(u"breakpoint_type_combobox")
        self.breakpoint_type_combobox.setGeometry(QRect(890, 110, 171, 24))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.breakpoint_add_button.setText(QCoreApplication.translate("Dialog", u"Add", None))
        self.breakpoint_delete_button.setText(QCoreApplication.translate("Dialog", u"Delete", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Compare the breakpoints defined by antimirobial susceptibility guidelines to the breakpoints used in your laboratory.", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Make any necessary changes.", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"To add additional species or antibiotics, select 'Add''.", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Organism", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Site of infection", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Antibiotic", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Test method", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Breakpoint type ", None))
        self.breakpoint_ok_button.setText(QCoreApplication.translate("Dialog", u"OK", None))
        self.breakpoint_cancel_button.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
    # retranslateUi

