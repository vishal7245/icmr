from PySide6.QtWidgets import QDialog, QListWidgetItem, QMessageBox
from modules.ui_add_antibiotic_profile_dialog import Ui_Dialog
from PySide6.QtCore import Qt, Signal
import pandas as pd

ANTIBIOTIC_CODE_ROLE = Qt.UserRole + 1
ANTIBIOTIC_NAME_ROLE = Qt.UserRole + 2
ANTIBIOTIC_POTENCY_ROLE = Qt.UserRole + 3
ANTIBIOTIC_FULL_NAME_ROLE = Qt.UserRole + 4
ANTIBIOTIC_GUIDELINES_ROLE = Qt.UserRole + 5
ANTIBIOTIC_TEST_ROLE = Qt.UserRole + 6

class AddAntibioticProfileDialog(QDialog):
    def __init__(self, data):
        super(AddAntibioticProfileDialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Add Antibiotic Profile")
        self.setWindowFlags(self.windowFlags() | Qt.Tool)
        self.setFixedSize(1080, 720)

        self.antibiotic_dataframe = data
        self.populate_local_antibiotic_list()
        
        # Signals
        self.ui.add_profile_antibiotics_button.clicked.connect(self.add_profile_antibiotics)
        self.ui.add_supplementary_button.clicked.connect(self.add_supplementary_antibiotics)
        self.ui.delete_profile_antibiotics_button.clicked.connect(self.remove_profile_antibiotics)
        self.ui.delete_supplementary_button.clicked.connect(self.remove_supplementary_antibiotics)
        self.ui.clear_profile_antibiotics.clicked.connect(self.clear_profile_antibiotics)
        self.ui.clear_list_supplementary.clicked.connect(self.clear_supplementary_antibiotics)
    


    def populate_local_antibiotic_list(self):
        for index, row in self.antibiotic_dataframe.iterrows():
            item = QListWidgetItem()
            item.setData(ANTIBIOTIC_CODE_ROLE, row['ANTIBIOTIC_CODE'])
            item.setData(ANTIBIOTIC_NAME_ROLE, row['ANTIBIOTIC_NAME'])
            item.setData(ANTIBIOTIC_POTENCY_ROLE, row['ANTIBIOTIC_POTENCY'])
            item.setData(ANTIBIOTIC_FULL_NAME_ROLE, row['ANTIBIOTIC_FULL_NAME'])
            item.setData(ANTIBIOTIC_GUIDELINES_ROLE, row['ANTIBIOTIC_GUIDELINES'])
            item.setData(ANTIBIOTIC_TEST_ROLE, row['ANTIBIOTIC_TEST'])
            item.setText(row['ANTIBIOTIC_FULL_NAME'])
            self.ui.local_antibiotics_list.addItem(item)

    def add_profile_antibiotics(self):
        selected_items = self.ui.local_antibiotics_list.selectedItems()
        for item in selected_items:
            item_clone = item.clone()
            self.ui.profile_antibiotics_list.addItem(item_clone)

            # check if item is already in the list
            num = self.ui.profile_antibiotics_list.count()
            if num > 1:
                for i in range(num-1):
                    profile_item = self.ui.profile_antibiotics_list.item(i)
                    if profile_item.data(ANTIBIOTIC_FULL_NAME_ROLE) == item.data(ANTIBIOTIC_FULL_NAME_ROLE):
                        QMessageBox.warning(self, "Warning", "Antibiotic already in profile.")
                        self.ui.profile_antibiotics_list.takeItem(num-1)
                        break

    def remove_profile_antibiotics(self):
        selected_items = self.ui.profile_antibiotics_list.selectedItems()
        for item in selected_items:
            self.ui.profile_antibiotics_list.takeItem(self.ui.profile_antibiotics_list.row(item))
    
    def add_supplementary_antibiotics(self):
        selected_items = self.ui.local_antibiotics_list.selectedItems()
        for item in selected_items:
            item_clone = item.clone()
            self.ui.supplementary_antibiotics_list.addItem(item_clone)

            # check if item is already in the list
            num = self.ui.supplementary_antibiotics_list.count()
            if num > 1:
                for i in range(num-1):
                    supplementary_item = self.ui.supplementary_antibiotics_list.item(i)
                    if supplementary_item.data(ANTIBIOTIC_FULL_NAME_ROLE) == item.data(ANTIBIOTIC_FULL_NAME_ROLE):
                        QMessageBox.warning(self, "Warning", "Antibiotic already in profile.")
                        self.ui.supplementary_antibiotics_list.takeItem(num-1)
                        break
    
    def remove_supplementary_antibiotics(self):
        selected_items = self.ui.supplementary_antibiotics_list.selectedItems()
        for item in selected_items:
            self.ui.supplementary_antibiotics_list.takeItem(self.ui.supplementary_antibiotics_list.row(item))

    def clear_profile_antibiotics(self):
        self.ui.profile_antibiotics_list.clear()

    def clear_supplementary_antibiotics(self):
        self.ui.supplementary_antibiotics_list.clear()
    

            


