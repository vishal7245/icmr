import csv, re
from PySide6.QtWidgets import QDialog
from modules.ui_breakpoint_dialog import Ui_Dialog
import pandas as pd

class BreakpointDialog(QDialog):
    def __init__(self, data):
        super(BreakpointDialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Breakpoints")
        
        