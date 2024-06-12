from PySide6.QtWidgets import QDialog
from modules.ui_antibiotic_panels_dialog import Ui_Dialog
from PySide6.QtCore import Qt, Signal
import pandas as pd

class AntibioticPanelsDialog(QDialog):
    def __init__(self):
        super(AntibioticPanelsDialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Antibiotic Panels")
        self.setWindowFlags(self.windowFlags() | Qt.Tool)
        self.setFixedSize(1080, 720)
        