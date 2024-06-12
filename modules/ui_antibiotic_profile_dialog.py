# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'antibiotic_profile_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1080, 717)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 1041, 16))
        self.antibiotic_profile_table = QTableWidget(Dialog)
        self.antibiotic_profile_table.setObjectName(u"antibiotic_profile_table")
        self.antibiotic_profile_table.setGeometry(QRect(10, 30, 1051, 641))
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(890, 680, 168, 26))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.ok_pushbutton = QPushButton(self.layoutWidget)
        self.ok_pushbutton.setObjectName(u"ok_pushbutton")

        self.horizontalLayout.addWidget(self.ok_pushbutton)

        self.cancel_pushbutton = QPushButton(self.layoutWidget)
        self.cancel_pushbutton.setObjectName(u"cancel_pushbutton")

        self.horizontalLayout.addWidget(self.cancel_pushbutton)

        self.layoutWidget1 = QWidget(Dialog)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 680, 168, 26))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.edit_pushbutton = QPushButton(self.layoutWidget1)
        self.edit_pushbutton.setObjectName(u"edit_pushbutton")

        self.horizontalLayout_2.addWidget(self.edit_pushbutton)

        self.add_pushbutton = QPushButton(self.layoutWidget1)
        self.add_pushbutton.setObjectName(u"add_pushbutton")

        self.horizontalLayout_2.addWidget(self.add_pushbutton)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"The analysis 'Resistant profiles' uses the below antibiotics to classify organisms according to their resistance phenotypes", None))
        self.ok_pushbutton.setText(QCoreApplication.translate("Dialog", u"OK", None))
        self.cancel_pushbutton.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.edit_pushbutton.setText(QCoreApplication.translate("Dialog", u"Edit", None))
        self.add_pushbutton.setText(QCoreApplication.translate("Dialog", u"Add", None))
    # retranslateUi

