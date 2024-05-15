# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lab_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(800, 600)
        self.tableWidget = QTableWidget(Dialog)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(20, 20, 511, 521))
        self.cancel_button = QPushButton(Dialog)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.setGeometry(QRect(550, 560, 231, 24))
        self.browse_button = QPushButton(Dialog)
        self.browse_button.setObjectName(u"browse_button")
        self.browse_button.setGeometry(QRect(450, 560, 80, 24))
        self.location_label = QLabel(Dialog)
        self.location_label.setObjectName(u"location_label")
        self.location_label.setGeometry(QRect(20, 560, 261, 21))
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(550, 20, 231, 191))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.new_laboratory = QPushButton(self.layoutWidget)
        self.new_laboratory.setObjectName(u"new_laboratory")

        self.verticalLayout.addWidget(self.new_laboratory)

        self.open_laboratory = QPushButton(self.layoutWidget)
        self.open_laboratory.setObjectName(u"open_laboratory")

        self.verticalLayout.addWidget(self.open_laboratory)

        self.modify_laboratory = QPushButton(self.layoutWidget)
        self.modify_laboratory.setObjectName(u"modify_laboratory")

        self.verticalLayout.addWidget(self.modify_laboratory)

        self.delete_laboratory = QPushButton(self.layoutWidget)
        self.delete_laboratory.setObjectName(u"delete_laboratory")

        self.verticalLayout.addWidget(self.delete_laboratory)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.cancel_button.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.browse_button.setText(QCoreApplication.translate("Dialog", u"Browse", None))
        self.location_label.setText(QCoreApplication.translate("Dialog", u"Location Label", None))
        self.new_laboratory.setText(QCoreApplication.translate("Dialog", u"New Laboratory", None))
        self.open_laboratory.setText(QCoreApplication.translate("Dialog", u"Open Laboratory", None))
        self.modify_laboratory.setText(QCoreApplication.translate("Dialog", u"Modify Laboratory", None))
        self.delete_laboratory.setText(QCoreApplication.translate("Dialog", u"Delete Laboratory", None))
    # retranslateUi

