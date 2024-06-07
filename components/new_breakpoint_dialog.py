import csv, re
from PySide6.QtWidgets import QDialog
from modules.ui_new_breakpoint_dialog import Ui_Dialog, QListWidgetItem
from PySide6.QtCore import Qt, Signal
import pandas as pd

ORGANISM_CODE_ROLE = Qt.UserRole + 1
ORGANISM_NAME_ROLE = Qt.UserRole + 2

class NewBreakpointDialog(QDialog):

    data_accepted = Signal(str, str, str)

    def __init__(self, data):
        super(NewBreakpointDialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("New Breakpoint")
        self.setWindowFlags(self.windowFlags() | Qt.Tool)
        self.setFixedSize(800, 600)
        self.data = data
        
        # Component Logic
        self.populate_antibiotic_list(self.data)
        self.populate_organism_list()
        self.ui.antibiotic_code_lineedit.setReadOnly(True)
        self.ui.organism_code_lineedit.setReadOnly(True)
        self.ui.short_list_radio_button.setChecked(True)
        


        # Signals
        self.ui.new_breakpoint_antibiotic_list.itemSelectionChanged.connect(self.update_antibiotic_code)
        self.ui.new_breakpoint_organism_list.itemSelectionChanged.connect(self.update_organism_code)
        self.ui.short_list_radio_button.toggled.connect(self.populate_organism_list)
        self.ui.extended_list_radiobutton.toggled.connect(self.populate_organism_list)
        self.ui.organism_group_radio_button.toggled.connect(self.populate_organism_list)

        self.ui.new_breakpoint_ok_button.clicked.connect(self.accept_data)
        self.ui.new_breakpoint_cancel_button.clicked.connect(self.reject)

        


    def populate_antibiotic_list(self, data):
        antibiotics = data['ANTIBIOTIC_FULL_NAME'].unique()
        for antibiotic in antibiotics:
            self.ui.new_breakpoint_antibiotic_list.addItem(antibiotic)


    def update_antibiotic_code(self):
        antibiotic = self.ui.new_breakpoint_antibiotic_list.currentItem().text()
        for index, row in self.data.iterrows():
            if row['ANTIBIOTIC_FULL_NAME'] == antibiotic:
                code = row['ANTIBIOTIC_CODES']
                self.ui.antibiotic_code_lineedit.setText(code)
                break

    def populate_organism_list(self):
        self.ui.new_breakpoint_organism_list.clear()
        filename = 'data/short_organism_list.csv'
        if self.ui.short_list_radio_button.isChecked():
            filename = 'data/short_organism_list.csv'
        elif self.ui.extended_list_radiobutton.isChecked():
            filename = 'data/extended_organism_list.csv'
        elif self.ui.organism_group_radio_button.isChecked():
            filename = 'data/organism_group_list.csv'
        with open(filename, newline="") as fcsv:
            reader = csv.reader(fcsv)
            for row in reader:
                item = QListWidgetItem()
                item.setData(ORGANISM_CODE_ROLE, row[0])
                item.setData(ORGANISM_NAME_ROLE, row[1])
                item.setText(row[0] + '\t' +row[1])
                self.ui.new_breakpoint_organism_list.addItem(item)

    def update_organism_code(self):
        organism = self.ui.new_breakpoint_organism_list.currentItem()
        code = organism.data(ORGANISM_CODE_ROLE)
        self.ui.organism_code_lineedit.setText(code)

    def accept_data(self):
        selected_antibiotic = self.ui.new_breakpoint_antibiotic_list.currentItem().text()
        selected_organism = self.ui.new_breakpoint_organism_list.currentItem().data(ORGANISM_NAME_ROLE)
        selected_organism_code = self.ui.organism_code_lineedit.text()

        self.data_accepted.emit(selected_antibiotic, selected_organism, selected_organism_code)

        self.accept()


    