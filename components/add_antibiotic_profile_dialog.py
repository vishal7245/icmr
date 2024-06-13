from PySide6.QtWidgets import QDialog, QListWidgetItem, QMessageBox
from modules.ui_add_antibiotic_profile_dialog import Ui_Dialog
from PySide6.QtCore import Qt, Signal
import pandas as pd
import re

ANTIBIOTIC_CODE_ROLE = Qt.UserRole + 1
ANTIBIOTIC_NAME_ROLE = Qt.UserRole + 2
ANTIBIOTIC_POTENCY_ROLE = Qt.UserRole + 3
ANTIBIOTIC_FULL_NAME_ROLE = Qt.UserRole + 4
ANTIBIOTIC_GUIDELINES_ROLE = Qt.UserRole + 5
ANTIBIOTIC_TEST_ROLE = Qt.UserRole + 6

class AddAntibioticProfileDialog(QDialog):

    profile_signal = Signal(str, str, int, int)
 
    def __init__(self, data, row, column, row_data):
        super(AddAntibioticProfileDialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Add Antibiotic Profile")
        self.setWindowFlags(self.windowFlags() | Qt.Tool)
        self.setFixedSize(1080, 720)

        self.antibiotic_dataframe = data
        self.row = row
        self.column = column
        self.row_data = row_data
        self.populate_local_antibiotic_list()

        # Re-populate the profile and supplementary list if the row_data is not empty
        if row_data:
            if "(" in row_data:
                profile_list, supplementary_list = self.parse_and_populate_profile_and_supplementary()
                self.re_populate_antibiotics(profile_list, supplementary_list)
            else:
                profile_list = self.parse_and_populate_profile_only()
                supplementary_list = []
                self.re_populate_antibiotics(profile_list, supplementary_list)
        
        # Signals
        self.ui.add_profile_antibiotics_button.clicked.connect(self.add_profile_antibiotics)
        self.ui.add_supplementary_button.clicked.connect(self.add_supplementary_antibiotics)
        self.ui.delete_profile_antibiotics_button.clicked.connect(self.remove_profile_antibiotics)
        self.ui.delete_supplementary_button.clicked.connect(self.remove_supplementary_antibiotics)
        self.ui.clear_profile_antibiotics.clicked.connect(self.clear_profile_antibiotics)
        self.ui.clear_list_supplementary.clicked.connect(self.clear_supplementary_antibiotics)
        self.ui.ok_pushbutton.clicked.connect(self.accept_data)
        self.ui.cancel_pushbutton.clicked.connect(self.reject)

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

    def re_populate_antibiotics(self, profile_list, supplementary_list):
        if len(profile_list) > 0:
            for antibiotic_code in profile_list:
                for index, row in self.antibiotic_dataframe.iterrows():
                    if row['ANTIBIOTIC_CODE'] == antibiotic_code:
                        item = QListWidgetItem()
                        item.setData(ANTIBIOTIC_CODE_ROLE, row['ANTIBIOTIC_CODE'])
                        item.setData(ANTIBIOTIC_NAME_ROLE, row['ANTIBIOTIC_NAME'])
                        item.setData(ANTIBIOTIC_POTENCY_ROLE, row['ANTIBIOTIC_POTENCY'])
                        item.setData(ANTIBIOTIC_FULL_NAME_ROLE, row['ANTIBIOTIC_FULL_NAME'])
                        item.setData(ANTIBIOTIC_GUIDELINES_ROLE, row['ANTIBIOTIC_GUIDELINES'])
                        item.setData(ANTIBIOTIC_TEST_ROLE, row['ANTIBIOTIC_TEST'])
                        item.setText(row['ANTIBIOTIC_FULL_NAME'])
                        self.ui.profile_antibiotics_list.addItem(item)
        
        if len(supplementary_list) > 0:
            for antibiotic_code in supplementary_list:
                for index, row in self.antibiotic_dataframe.iterrows():
                    if row['ANTIBIOTIC_CODE'] == antibiotic_code:
                        item = QListWidgetItem()
                        item.setData(ANTIBIOTIC_CODE_ROLE, row['ANTIBIOTIC_CODE'])
                        item.setData(ANTIBIOTIC_NAME_ROLE, row['ANTIBIOTIC_NAME'])
                        item.setData(ANTIBIOTIC_POTENCY_ROLE, row['ANTIBIOTIC_POTENCY'])
                        item.setData(ANTIBIOTIC_FULL_NAME_ROLE, row['ANTIBIOTIC_FULL_NAME'])
                        item.setData(ANTIBIOTIC_GUIDELINES_ROLE, row['ANTIBIOTIC_GUIDELINES'])
                        item.setData(ANTIBIOTIC_TEST_ROLE, row['ANTIBIOTIC_TEST'])
                        item.setText(row['ANTIBIOTIC_FULL_NAME'])
                        self.ui.supplementary_antibiotics_list.addItem(item)

    def add_antibiotic(self, source_list, target_list):
        selected_items = source_list.selectedItems()
        for item in selected_items:
            # Check for duplicates in the target list
            if self.is_duplicate_in_list(item, target_list):
                QMessageBox.warning(self, "Warning", "Antibiotic already in profile.")
                continue
            # Check for duplicates in the complementary list
            complementary_list = self.get_complementary_list(target_list)
            if self.is_duplicate_in_list(item, complementary_list):
                QMessageBox.warning(self, "Warning", "Antibiotic already in profile.")
                continue
            # Clone and add the item if no duplicates found
            item_clone = item.clone()
            target_list.addItem(item_clone)

    def is_duplicate_in_list(self, item, target_list):
        num_items = target_list.count()
        for i in range(num_items):
            target_item = target_list.item(i)
            if target_item.data(ANTIBIOTIC_FULL_NAME_ROLE) == item.data(ANTIBIOTIC_FULL_NAME_ROLE):
                return True
        return False

    def get_complementary_list(self, target_list):
        if target_list == self.ui.profile_antibiotics_list:
            return self.ui.supplementary_antibiotics_list
        elif target_list == self.ui.supplementary_antibiotics_list:
            return self.ui.profile_antibiotics_list
        else:
            raise ValueError("Unknown target list")

    def add_profile_antibiotics(self):
        self.add_antibiotic(self.ui.local_antibiotics_list, self.ui.profile_antibiotics_list)

    def add_supplementary_antibiotics(self):
        self.add_antibiotic(self.ui.local_antibiotics_list, self.ui.supplementary_antibiotics_list)

    def remove_profile_antibiotics(self):
        selected_items = self.ui.profile_antibiotics_list.selectedItems()
        for item in selected_items:
            self.ui.profile_antibiotics_list.takeItem(self.ui.profile_antibiotics_list.row(item))

    def remove_supplementary_antibiotics(self):
        selected_items = self.ui.supplementary_antibiotics_list.selectedItems()
        for item in selected_items:
            self.ui.supplementary_antibiotics_list.takeItem(self.ui.supplementary_antibiotics_list.row(item))

    def clear_profile_antibiotics(self):
        self.ui.profile_antibiotics_list.clear()

    def clear_supplementary_antibiotics(self):
        self.ui.supplementary_antibiotics_list.clear()

    def list_to_comma_separated_string(self, input_list):
        return ', '.join(map(str, input_list))
    
    def parse_and_populate_profile_only(self):
        data_list = [x.strip() for x in self.row_data.split(",")]
        return data_list
    
    def parse_and_populate_profile_and_supplementary(self):
        supplementary = re.findall(r'\((.*?)\)', self.row_data)
        supplementary_string = ', '.join(supplementary)

        # Split the profile and supplementary string
        supplementary_list = [item.strip() for item in supplementary_string.split(',') if item.strip()]
        profile_list = [item.strip() for item in re.sub(r'\(.*?\)', '', self.row_data).split(',') if item.strip()]

        return profile_list, supplementary_list


        

    def accept_data(self):
        ANTIBIOTIC_CODE = []
        ANTIBIOTIC_FULL_NAME = []
        ANTIBIOTIC_NAME_ = []
        ANTIBIOTIC_GUIDELINES = []
        ANTIBIOTIC_TEST = []
        ANTIBIOTIC_POTENCY = []

        for index in range(self.ui.profile_antibiotics_list.count()):
            item = self.ui.profile_antibiotics_list.item(index)
            ANTIBIOTIC_CODE.append(item.data(ANTIBIOTIC_CODE_ROLE))
            ANTIBIOTIC_FULL_NAME.append(item.data(ANTIBIOTIC_FULL_NAME_ROLE))
            ANTIBIOTIC_NAME_.append(item.data(ANTIBIOTIC_NAME_ROLE))
            ANTIBIOTIC_GUIDELINES.append(item.data(ANTIBIOTIC_GUIDELINES_ROLE))
            ANTIBIOTIC_TEST.append(item.data(ANTIBIOTIC_TEST_ROLE))
            ANTIBIOTIC_POTENCY.append(item.data(ANTIBIOTIC_POTENCY_ROLE))

        data = {
            "ANTIBIOTIC_CODE": ANTIBIOTIC_CODE,
            "ANTIBIOTIC_FULL_NAME": ANTIBIOTIC_FULL_NAME,
            "ANTIBIOTIC_NAME": ANTIBIOTIC_NAME_,
            "ANTIBIOTIC_GUIDELINES": ANTIBIOTIC_GUIDELINES,
            "ANTIBIOTIC_TEST": ANTIBIOTIC_TEST,
            "ANTIBIOTIC_POTENCY": ANTIBIOTIC_POTENCY
        }

        profile_antibiotics_df = pd.DataFrame(data)

        ANTIBIOTIC_CODE = []
        ANTIBIOTIC_FULL_NAME = []
        ANTIBIOTIC_NAME_ = []
        ANTIBIOTIC_GUIDELINES = []
        ANTIBIOTIC_TEST = []
        ANTIBIOTIC_POTENCY = []

        for index in range(self.ui.supplementary_antibiotics_list.count()):
            item = self.ui.supplementary_antibiotics_list.item(index)
            ANTIBIOTIC_CODE.append(item.data(ANTIBIOTIC_CODE_ROLE))
            ANTIBIOTIC_FULL_NAME.append(item.data(ANTIBIOTIC_FULL_NAME_ROLE))
            ANTIBIOTIC_NAME_.append(item.data(ANTIBIOTIC_NAME_ROLE))
            ANTIBIOTIC_GUIDELINES.append(item.data(ANTIBIOTIC_GUIDELINES_ROLE))
            ANTIBIOTIC_TEST.append(item.data(ANTIBIOTIC_TEST_ROLE))
            ANTIBIOTIC_POTENCY.append(item.data(ANTIBIOTIC_POTENCY_ROLE))

        data = {
            "ANTIBIOTIC_CODE": ANTIBIOTIC_CODE,
            "ANTIBIOTIC_FULL_NAME": ANTIBIOTIC_FULL_NAME,
            "ANTIBIOTIC_NAME": ANTIBIOTIC_NAME_,
            "ANTIBIOTIC_GUIDELINES": ANTIBIOTIC_GUIDELINES,
            "ANTIBIOTIC_TEST": ANTIBIOTIC_TEST,
            "ANTIBIOTIC_POTENCY": ANTIBIOTIC_POTENCY
        }

        supplementary_antibiotics_df = pd.DataFrame(data)

        profile_csv = profile_antibiotics_df.to_csv(index=False)
        if len(supplementary_antibiotics_df) == 0:
            supplementary_csv = "None"
        else:
            supplementary_csv = supplementary_antibiotics_df.to_csv(index=False)
        
        self.profile_signal.emit(profile_csv, supplementary_csv, self.row, self.column)
        
        self.accept()
