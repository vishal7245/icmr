# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_field_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QSpinBox,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(800, 600)
        self.add_datafield = QPushButton(Dialog)
        self.add_datafield.setObjectName(u"add_datafield")
        self.add_datafield.setGeometry(QRect(360, 160, 81, 31))
        self.remove_datafield = QPushButton(Dialog)
        self.remove_datafield.setObjectName(u"remove_datafield")
        self.remove_datafield.setGeometry(QRect(360, 240, 81, 31))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 30, 771, 16))
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(610, 560, 181, 26))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.ok_datafield_pushbutton = QPushButton(self.layoutWidget)
        self.ok_datafield_pushbutton.setObjectName(u"ok_datafield_pushbutton")

        self.horizontalLayout.addWidget(self.ok_datafield_pushbutton)

        self.cancel_datafield_pushbutton = QPushButton(self.layoutWidget)
        self.cancel_datafield_pushbutton.setObjectName(u"cancel_datafield_pushbutton")

        self.horizontalLayout.addWidget(self.cancel_datafield_pushbutton)

        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(450, 60, 331, 481))
        self.selected_datafield_list = QListWidget(self.groupBox)
        self.selected_datafield_list.setObjectName(u"selected_datafield_list")
        self.selected_datafield_list.setGeometry(QRect(10, 30, 311, 441))
        self.groupBox_2 = QGroupBox(Dialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 60, 341, 331))
        self.all_datafield_list = QListWidget(self.groupBox_2)
        self.all_datafield_list.setObjectName(u"all_datafield_list")
        self.all_datafield_list.setGeometry(QRect(10, 30, 321, 291))
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 400, 341, 141))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.search_datafield = QLineEdit(self.frame)
        self.search_datafield.setObjectName(u"search_datafield")
        self.search_datafield.setGeometry(QRect(60, 10, 271, 23))
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 13, 51, 20))
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 50, 91, 16))
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 70, 56, 16))
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 90, 56, 16))
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 110, 56, 16))
        self.datafield_description = QLabel(self.frame)
        self.datafield_description.setObjectName(u"datafield_description")
        self.datafield_description.setGeometry(QRect(90, 50, 241, 16))
        self.datafield_name = QLabel(self.frame)
        self.datafield_name.setObjectName(u"datafield_name")
        self.datafield_name.setGeometry(QRect(90, 70, 241, 16))
        self.datafield_type = QLabel(self.frame)
        self.datafield_type.setObjectName(u"datafield_type")
        self.datafield_type.setGeometry(QRect(90, 90, 241, 16))
        self.datafield_length_spinbox = QSpinBox(self.frame)
        self.datafield_length_spinbox.setObjectName(u"datafield_length_spinbox")
        self.datafield_length_spinbox.setGeometry(QRect(90, 110, 61, 24))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.add_datafield.setText(QCoreApplication.translate("Dialog", u"->", None))
        self.remove_datafield.setText(QCoreApplication.translate("Dialog", u"<-", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Your data fields appear below to the right. You may include additional fields from the MicroTrack list to the left.", None))
        self.ok_datafield_pushbutton.setText(QCoreApplication.translate("Dialog", u"OK", None))
        self.cancel_datafield_pushbutton.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Selected Fields", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"All Fields", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Search:", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Description:", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Name:", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Type:", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Length:", None))
        self.datafield_description.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.datafield_name.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.datafield_type.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
    # retranslateUi

