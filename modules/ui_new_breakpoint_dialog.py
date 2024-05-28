# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_breakpoint_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QPushButton, QRadioButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(800, 600)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 491, 16))
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 90, 381, 461))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 10, 101, 16))
        self.new_breakpoint_organism_list = QListWidget(self.frame)
        self.new_breakpoint_organism_list.setObjectName(u"new_breakpoint_organism_list")
        self.new_breakpoint_organism_list.setGeometry(QRect(10, 70, 361, 381))
        self.extended_list_radiobutton = QRadioButton(self.frame)
        self.extended_list_radiobutton.setObjectName(u"extended_list_radiobutton")
        self.extended_list_radiobutton.setGeometry(QRect(120, 40, 99, 22))
        self.organism_group_radio_button = QRadioButton(self.frame)
        self.organism_group_radio_button.setObjectName(u"organism_group_radio_button")
        self.organism_group_radio_button.setGeometry(QRect(250, 40, 121, 22))
        self.short_list_radio_button = QRadioButton(self.frame)
        self.short_list_radio_button.setObjectName(u"short_list_radio_button")
        self.short_list_radio_button.setGeometry(QRect(10, 40, 99, 22))
        self.frame_2 = QFrame(Dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(400, 90, 391, 461))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 10, 211, 16))
        self.new_breakpoint_antibiotic_list = QListWidget(self.frame_2)
        self.new_breakpoint_antibiotic_list.setObjectName(u"new_breakpoint_antibiotic_list")
        self.new_breakpoint_antibiotic_list.setGeometry(QRect(10, 70, 371, 381))
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(170, 50, 91, 20))
        self.organism_code_lineedit = QLineEdit(Dialog)
        self.organism_code_lineedit.setObjectName(u"organism_code_lineedit")
        self.organism_code_lineedit.setGeometry(QRect(270, 50, 113, 23))
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(580, 50, 91, 20))
        self.antibiotic_code_lineedit = QLineEdit(Dialog)
        self.antibiotic_code_lineedit.setObjectName(u"antibiotic_code_lineedit")
        self.antibiotic_code_lineedit.setGeometry(QRect(680, 50, 113, 23))
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(620, 560, 168, 26))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.new_breakpoint_ok_button = QPushButton(self.widget)
        self.new_breakpoint_ok_button.setObjectName(u"new_breakpoint_ok_button")

        self.horizontalLayout.addWidget(self.new_breakpoint_ok_button)

        self.new_breakpoint_cancel_button = QPushButton(self.widget)
        self.new_breakpoint_cancel_button.setObjectName(u"new_breakpoint_cancel_button")

        self.horizontalLayout.addWidget(self.new_breakpoint_cancel_button)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Click on the organism and the antibiotic for the new breakpoint.", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Organism List", None))
        self.extended_list_radiobutton.setText(QCoreApplication.translate("Dialog", u"Extended list", None))
        self.organism_group_radio_button.setText(QCoreApplication.translate("Dialog", u"Organism groups", None))
        self.short_list_radio_button.setText(QCoreApplication.translate("Dialog", u"Short list", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Antibiotic List", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Organism code:", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Antibiotic code:", None))
        self.new_breakpoint_ok_button.setText(QCoreApplication.translate("Dialog", u"OK", None))
        self.new_breakpoint_cancel_button.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
    # retranslateUi

