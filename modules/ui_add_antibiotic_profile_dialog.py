# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_antibiotic_profile_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QGroupBox, QHBoxLayout,
    QLabel, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1080, 720)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 951, 16))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 30, 881, 16))
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 80, 491, 581))
        self.local_antibiotics_list = QListWidget(self.groupBox)
        self.local_antibiotics_list.setObjectName(u"local_antibiotics_list")
        self.local_antibiotics_list.setGeometry(QRect(10, 30, 471, 541))
        self.groupBox_2 = QGroupBox(Dialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(590, 80, 471, 291))
        self.profile_antibiotics_list = QListWidget(self.groupBox_2)
        self.profile_antibiotics_list.setObjectName(u"profile_antibiotics_list")
        self.profile_antibiotics_list.setGeometry(QRect(10, 60, 451, 221))
        self.clear_profile_antibiotics = QPushButton(self.groupBox_2)
        self.clear_profile_antibiotics.setObjectName(u"clear_profile_antibiotics")
        self.clear_profile_antibiotics.setGeometry(QRect(380, 30, 80, 24))
        self.groupBox_3 = QGroupBox(Dialog)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(590, 380, 471, 281))
        self.supplementary_antibiotics_list = QListWidget(self.groupBox_3)
        self.supplementary_antibiotics_list.setObjectName(u"supplementary_antibiotics_list")
        self.supplementary_antibiotics_list.setGeometry(QRect(10, 60, 451, 211))
        self.clear_list_supplementary = QPushButton(self.groupBox_3)
        self.clear_list_supplementary.setObjectName(u"clear_list_supplementary")
        self.clear_list_supplementary.setGeometry(QRect(380, 30, 80, 24))
        self.add_profile_antibiotics_button = QPushButton(Dialog)
        self.add_profile_antibiotics_button.setObjectName(u"add_profile_antibiotics_button")
        self.add_profile_antibiotics_button.setGeometry(QRect(520, 170, 51, 31))
        self.delete_profile_antibiotics_button = QPushButton(Dialog)
        self.delete_profile_antibiotics_button.setObjectName(u"delete_profile_antibiotics_button")
        self.delete_profile_antibiotics_button.setGeometry(QRect(520, 220, 51, 31))
        self.add_supplementary_button = QPushButton(Dialog)
        self.add_supplementary_button.setObjectName(u"add_supplementary_button")
        self.add_supplementary_button.setGeometry(QRect(520, 490, 51, 31))
        self.delete_supplementary_button = QPushButton(Dialog)
        self.delete_supplementary_button.setObjectName(u"delete_supplementary_button")
        self.delete_supplementary_button.setGeometry(QRect(520, 540, 51, 31))
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(890, 680, 168, 26))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Indicate which antibiotics to use in the resistance profile (profile antibiotics).", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"You may also include additional antibiotics which will appear in the resistance profile listing (supplementary antibiotics).", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Local antibiotic list", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"Profile antibiotics", None))
        self.clear_profile_antibiotics.setText(QCoreApplication.translate("Dialog", u"Clear List", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Dialog", u"Supplementary antibiotics", None))
        self.clear_list_supplementary.setText(QCoreApplication.translate("Dialog", u"Clear List", None))
        self.add_profile_antibiotics_button.setText(QCoreApplication.translate("Dialog", u"->", None))
        self.delete_profile_antibiotics_button.setText(QCoreApplication.translate("Dialog", u"<-", None))
        self.add_supplementary_button.setText(QCoreApplication.translate("Dialog", u"->", None))
        self.delete_supplementary_button.setText(QCoreApplication.translate("Dialog", u"<-", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"OK", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
    # retranslateUi

