import sys, csv, re
from PySide6.QtWidgets import QDialog, QAbstractItemView, QListWidgetItem, QMessageBox, QHeaderView, QTableWidgetItem
from modules.ui_new_lab_dialog import Ui_Dialog
from components.breakpoint_dialog import BreakpointDialog
from PySide6.QtCore import Qt
import pandas as pd
from io import StringIO

# custom roles
ANTIBIOTIC_CODE_ROLE = Qt.UserRole + 1
ANTIBIOTIC_NAME_ROLE = Qt.UserRole + 2
ANTIBIOTIC_POTENCY_ROLE = Qt.UserRole + 3
ANTIBIOTIC_FULL_NAME_ROLE = Qt.UserRole + 4
ANTIBIOTIC_GUIDELINES_ROLE = Qt.UserRole + 5
ANTIBIOTIC_TEST_ROLE = Qt.UserRole + 6

DEPARTMENT_CODE_ROLE = Qt.UserRole + 1
DEPARTMENT_NAME_ROLE = Qt.UserRole + 2

LOCATION_TYPE_CODE_ROLE = Qt.UserRole + 1
LOCATION_TYPE_NAME_ROLE = Qt.UserRole + 2

class NewLabDialog(QDialog):
    def __init__(self):
        super(NewLabDialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.populate_country_combobox()
        self.populate_antibiotic_list()
        self.populate_departments()
        self.populate_location_type()

        self.ui.tabWidget.setCurrentIndex(0)
        self.setFixedSize(1080, 600)
        self.setWindowTitle("New Laboratory")

        # Form Components
        self.ui.general_human_radio.setChecked(True)
        self.ui.general_country_code.setText("")
        self.ui.general_configfile_name.setText("")
        self.ui.antibiotics_full_name.setText("")
        self.ui.antibiotic_guidelines_combobox.addItems(["CLSI 2023(United States)", "EUCAST 2023(Europe)"])
        self.ui.antibiotics_disk_radio.setChecked(True)

        # Location Table View
        self.ui.location_table_list.setColumnCount(5)
        self.ui.location_table_list.setHorizontalHeaderLabels(["Location name","Code","Institution","Department","Location Type"])
        self.ui.location_table_list.verticalHeader().setVisible(False)
        self.ui.location_table_list.insertRow(0)
        self.selected_row = None

        header = self.ui.location_table_list.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.Stretch)
        header.setSectionResizeMode(3, QHeaderView.Stretch)
        header.setSectionResizeMode(4, QHeaderView.Stretch)

        # Connecting Signals
        self.ui.general_country_combobox.currentIndexChanged.connect(self.update_country_info)
        self.ui.general_labcode_lineedit.textChanged.connect(self.update_configuration_label)
        self.ui.antibiotics_add_button.clicked.connect(self.move_antibiotic_right)
        self.ui.antibiotics_add_button.clicked.connect(self.update_num_antibiotics_label)
        self.ui.antibiotics_remove_button.clicked.connect(self.remove_antibiotic)
        self.ui.antibiotic_local_list.itemSelectionChanged.connect(self.update_fullname_label)
        self.ui.antibiotic_guidelines_combobox.currentIndexChanged.connect(self.update_fullname_label)
        self.ui.antibiotics_disk_radio.clicked.connect(self.update_fullname_label)
        self.ui.antibiotics_mic_radio.clicked.connect(self.update_fullname_label)
        self.ui.antibiotics_etest_radio.clicked.connect(self.update_fullname_label)
        self.ui.antibiotics_remove_button.clicked.connect(self.update_num_antibiotics_label)
        self.ui.antibiotics_remove_button.clicked.connect(self.update_fullname_label)
        self.ui.antibiotics_search.textChanged.connect(self.search_antibiotics)
        self.ui.location_table_list.itemSelectionChanged.connect(self.selected_location_tablelist)
        self.ui.location_table_list.cellChanged.connect(self.add_row_location_table)
        self.ui.department_listview.itemClicked.connect(self.update_department)
        self.ui.location_type_listview.itemClicked.connect(self.update_location_type)
        self.ui.location_table_list.cellChanged.connect(self.select_row_on_edit)
        self.ui.antibiotics_breakpoint_button.clicked.connect(self.open_breakpoint_dialog)

        # Store original antibiotics
        self.original_antibiotics = []
        for i in range(self.ui.antibiotic_list.count()):
            item = self.ui.antibiotic_list.item(i)
            self.original_antibiotics.append((item.text(), item.data(ANTIBIOTIC_NAME_ROLE), item.data(ANTIBIOTIC_CODE_ROLE), item.data(ANTIBIOTIC_POTENCY_ROLE)))

    def populate_country_combobox(self):
        with open("data/COUNTRY.csv", newline="") as countrycsv:
            reader = csv.reader(countrycsv, delimiter='\t')
            next(reader)  # skip header row
            for row in reader:
                self.ui.general_country_combobox.addItem(row[3], row[0])  # Add item with code as userData

    def update_country_info(self):
        selected_index = self.ui.general_country_combobox.currentIndex()
        country_code = self.ui.general_country_combobox.itemData(selected_index)  # Get country code from userData
        self.ui.general_country_code.setText(country_code)
        self.update_configuration_label()  # Update config label

    def update_configuration_label(self):
        country_code = self.ui.general_country_code.text()
        lab_code = self.ui.general_labcode_lineedit.text()
        if country_code and lab_code:
            self.ui.general_configfile_name.setText(f"{country_code}{lab_code}.sqlite")

    def onFocusOutEvent(self, event):
        self.ui.general_labcode_lineedit.clearFocus()

    def populate_antibiotic_list(self):
        with open("data/Antibiotics.csv", newline="") as antibioticslist:
            reader = csv.reader(antibioticslist, delimiter='\t')
            next(reader)
            for row in reader:
                item = QListWidgetItem()

                # Set data
                item.setData(ANTIBIOTIC_NAME_ROLE, row[6])
                item.setData(ANTIBIOTIC_CODE_ROLE, row[0])
                if row[17] == "":
                    item.setData(ANTIBIOTIC_POTENCY_ROLE, 0)
                else:
                    item.setData(ANTIBIOTIC_POTENCY_ROLE, row[17])
                    
                # Set text after setting data
                if row[7] == "":
                    if row[17] == "":
                        item.setText(row[6])
                    else:
                        item.setText(f"{row[6]} ({row[17]})")
                else:
                    if row[17] == "":
                        item.setText(f"{row[6]} ({row[7]})")
                    else:
                        item.setText(f"{row[6]} ({row[7]}-{row[17]})")

                self.ui.antibiotic_list.addItem(item)

    def move_antibiotic_right(self):
        selected_items = self.ui.antibiotic_list.selectedItems()
        for item in selected_items:
            cloned_item = QListWidgetItem(item)
            self.ui.antibiotic_local_list.addItem(cloned_item)
            selected_guidelines = self.ui.antibiotic_guidelines_combobox.currentText()
            if selected_guidelines == "CLSI 2023(United States)":
                selected_guidelines = "N"
                cloned_item.setData(ANTIBIOTIC_GUIDELINES_ROLE, "CLSI")
            else:
                selected_guidelines = "E"
                cloned_item.setData(ANTIBIOTIC_GUIDELINES_ROLE, "EUCAST")
            selected_radio = ""
            if self.ui.antibiotics_disk_radio.isChecked():
                selected_radio = "D"
                cloned_item.setData(ANTIBIOTIC_TEST_ROLE, "Disk")
            elif self.ui.antibiotics_mic_radio.isChecked():
                selected_radio = "M"
                cloned_item.setData(ANTIBIOTIC_TEST_ROLE, "MIC")
            elif self.ui.antibiotics_etest_radio.isChecked():
                selected_radio = "E"
                cloned_item.setData(ANTIBIOTIC_TEST_ROLE, "Etest")
            if cloned_item.data(ANTIBIOTIC_POTENCY_ROLE) == 0:
                updated_code = cloned_item.data(ANTIBIOTIC_CODE_ROLE) +"_"+ selected_guidelines + selected_radio
            else:
                potency_match = re.search(r"^\d+(?=/)", cloned_item.data(ANTIBIOTIC_POTENCY_ROLE))
                if potency_match:
                    potency = potency_match.group()
                else:
                    potency_fallback = re.search(r"\d+", cloned_item.data(ANTIBIOTIC_POTENCY_ROLE))                          # Fallback if no potency value found
                    potency = potency_fallback.group()
                if selected_radio == "D":
                    updated_code = cloned_item.data(ANTIBIOTIC_CODE_ROLE) +"_"+ selected_guidelines + selected_radio + potency
                else:
                    updated_code = cloned_item.data(ANTIBIOTIC_CODE_ROLE) +"_"+ selected_guidelines + selected_radio 
            cloned_item.setData(ANTIBIOTIC_CODE_ROLE, updated_code)
            cloned_item.setText(cloned_item.data(ANTIBIOTIC_CODE_ROLE)+"\t"+ cloned_item.data(ANTIBIOTIC_NAME_ROLE))
            if cloned_item.data(ANTIBIOTIC_POTENCY_ROLE) == 0:
                cloned_item.setData(ANTIBIOTIC_FULL_NAME_ROLE, cloned_item.data(ANTIBIOTIC_NAME_ROLE) +"_"+ cloned_item.data(ANTIBIOTIC_GUIDELINES_ROLE) +"_"+ cloned_item.data(ANTIBIOTIC_TEST_ROLE))
            else:
                cloned_item.setData(ANTIBIOTIC_FULL_NAME_ROLE, cloned_item.data(ANTIBIOTIC_NAME_ROLE) +"_"+ cloned_item.data(ANTIBIOTIC_GUIDELINES_ROLE) +"_"+ cloned_item.data(ANTIBIOTIC_TEST_ROLE) +"_"+ cloned_item.data(ANTIBIOTIC_POTENCY_ROLE))

            #Check if the antibiotic is already in the list
            num_antibiotics = self.ui.antibiotic_local_list.count()
            if num_antibiotics > 1:
                for i in range(num_antibiotics-1):
                    item = self.ui.antibiotic_local_list.item(i)
                    if item.data(ANTIBIOTIC_CODE_ROLE) == updated_code:
                        QMessageBox.warning(self, "Warning", "Antibiotic already in the list", QMessageBox.Ok)
                        self.ui.antibiotic_local_list.takeItem(self.ui.antibiotic_local_list.row(cloned_item))
                        break

    def remove_antibiotic(self):
        selected_items = self.ui.antibiotic_local_list.selectedItems()
        for item in selected_items:
            self.ui.antibiotic_local_list.takeItem(self.ui.antibiotic_local_list.row(item))

    def update_num_antibiotics_label(self):
        num_antibiotics = self.ui.antibiotic_local_list.count()
        self.ui.num_antibiotics.setText(str(num_antibiotics))

    def update_fullname_label(self):
        if self.ui.antibiotic_local_list.currentItem() is not None:
            selected_item = self.ui.antibiotic_local_list.currentItem()
            self.ui.antibiotics_full_name.setText(f"{selected_item.data(ANTIBIOTIC_FULL_NAME_ROLE)}")
        else:
            self.ui.antibiotics_full_name.clear()
    
    def search_antibiotics(self):
        filter_text = self.ui.antibiotics_search.text().lower()
        # Clear the list widget
        self.ui.antibiotic_list.clear()

        if not filter_text:
            # If search bar is empty, show all original antibiotics
            for text, name_data, code_data, potency_data in self.original_antibiotics:
                new_item = QListWidgetItem(text)
                new_item.setData(ANTIBIOTIC_NAME_ROLE, name_data)
                new_item.setData(ANTIBIOTIC_CODE_ROLE, code_data)
                new_item.setData(ANTIBIOTIC_POTENCY_ROLE, potency_data)
                self.ui.antibiotic_list.addItem(new_item)
        else:
            # Filter items based on the search text
            filtered_items = [
                (text, name_data, code_data, potency_data) for text, name_data, code_data, potency_data in self.original_antibiotics
                if name_data.lower().startswith(filter_text)
            ]
            for text, name_data, code_data, potency_data in filtered_items:
                new_item = QListWidgetItem(text)
                new_item.setData(ANTIBIOTIC_NAME_ROLE, name_data)
                new_item.setData(ANTIBIOTIC_CODE_ROLE, code_data)
                new_item.setData(ANTIBIOTIC_POTENCY_ROLE, potency_data)
                self.ui.antibiotic_list.addItem(new_item)

    def populate_departments(self):
        self.ui.department_listview.addItem("None")
        with open("data/DEPARTMENT.csv", newline="") as departmentcsv:
            reader = csv.reader(departmentcsv, delimiter='\t')
            next(reader)
            for row in reader:
                item = QListWidgetItem()
                item.setData(DEPARTMENT_CODE_ROLE, row[0])
                item.setData(DEPARTMENT_NAME_ROLE, row[1])
                item.setText(row[0]+ "\t"+ row[1])
                self.ui.department_listview.addItem(item)

    def populate_location_type(self):
        self.ui.location_type_listview.addItem("None")
        with open("data/LOCATION_TYPE.csv", newline="") as locationtypecsv:
            reader = csv.reader(locationtypecsv, delimiter='\t')
            next(reader)
            for row in reader:
                item = QListWidgetItem()
                item.setData(LOCATION_TYPE_CODE_ROLE, row[0])
                item.setData(LOCATION_TYPE_NAME_ROLE, row[1])
                item.setText(row[0]+ "\t"+ row[1])
                self.ui.location_type_listview.addItem(item)

    def add_row_location_table(self, row, column):
        if row == self.ui.location_table_list.rowCount() -1:
            for col in range(self.ui.location_table_list.columnCount()):
                item = self.ui.location_table_list.item(row,col)
                if item and item.text():
                    self.ui.location_table_list.insertRow(self.ui.location_table_list.rowCount())
                    break

    def selected_location_tablelist(self):
        selected_items = self.ui.location_table_list.selectedItems()
        if selected_items:
            self.selected_row = selected_items[0].row()
        else:
            self.selected_row = None

    def update_department(self, item):
        if self.selected_row is not None:
            self.ui.location_table_list.setItem(self.selected_row, 3, QTableWidgetItem(item.data(DEPARTMENT_CODE_ROLE)))

    def update_location_type(self, item):
        if self.selected_row is not None:
            self.ui.location_table_list.setItem(self.selected_row, 4, QTableWidgetItem(item.data(LOCATION_TYPE_CODE_ROLE)))

    def select_row_on_edit(self, row, column):
        self.selected_row = row
        self.ui.location_table_list.selectRow(row)

    def open_breakpoint_dialog(self):
        ANTIBIOTIC_CODES = []
        ANTIBIOTIC_FULL_NAME = []
        ANTIBIOTIC_NAME_ = []
        ANTIBIOTIC_GUIDELINES = []
        ANTIBIOTIC_TEST = []
        antibiotics_count = self.ui.antibiotic_local_list.count()
        if antibiotics_count == 0:
            QMessageBox.warning(self, "Warning", "No antibiotics selected", QMessageBox.Ok)
            return
        else:
            for index in range(self.ui.antibiotic_local_list.count()):
                item = self.ui.antibiotic_local_list.item(index)
                ANTIBIOTIC_CODES.append(item.data(ANTIBIOTIC_CODE_ROLE))
                ANTIBIOTIC_FULL_NAME.append(item.data(ANTIBIOTIC_FULL_NAME_ROLE))
                ANTIBIOTIC_NAME_.append(item.data(ANTIBIOTIC_NAME_ROLE))
                ANTIBIOTIC_GUIDELINES.append(item.data(ANTIBIOTIC_GUIDELINES_ROLE))
                ANTIBIOTIC_TEST.append(item.data(ANTIBIOTIC_TEST_ROLE))

        data = {
            "ANTIBIOTIC_CODES": ANTIBIOTIC_CODES,
            "ANTIBIOTIC_FULL_NAME": ANTIBIOTIC_FULL_NAME,
            "ANTIBIOTIC_NAME_": ANTIBIOTIC_NAME_,
            "ANTIBIOTIC_GUIDELINES": ANTIBIOTIC_GUIDELINES,
            "ANTIBIOTIC_TEST": ANTIBIOTIC_TEST
        }

        df = pd.DataFrame(data)
        breakpoint_dialog = BreakpointDialog(data=df)
        breakpoint_dialog.data_frame_signal.connect(self.handle_breakpoint_data)
        breakpoint_dialog.exec()

    def handle_breakpoint_data(self, data):
        df = pd.read_csv(StringIO(data))
        self.breakpoint_dataframe = df
        print(self.breakpoint_dataframe.head())