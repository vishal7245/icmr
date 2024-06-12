# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'antibiotic_panels_dialog.ui'
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
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1080, 720)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 1041, 16))
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 30, 1051, 641))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.antibiotic_panel_table = QTableWidget(self.frame)
        self.antibiotic_panel_table.setObjectName(u"antibiotic_panel_table")
        self.antibiotic_panel_table.setGeometry(QRect(10, 10, 1031, 621))
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(857, 680, 201, 26))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.ok_pushbutton = QPushButton(self.widget)
        self.ok_pushbutton.setObjectName(u"ok_pushbutton")

        self.horizontalLayout.addWidget(self.ok_pushbutton)

        self.cancel_pushbutton = QPushButton(self.widget)
        self.cancel_pushbutton.setObjectName(u"cancel_pushbutton")

        self.horizontalLayout.addWidget(self.cancel_pushbutton)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Indicate which antibiotics you usually test for each organism group.", None))
        self.ok_pushbutton.setText(QCoreApplication.translate("Dialog", u"OK", None))
        self.cancel_pushbutton.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
    # retranslateUi

