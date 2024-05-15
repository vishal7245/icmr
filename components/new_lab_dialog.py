import sys, csv, re
from PySide6.QtWidgets import QDialog, QAbstractItemView, QListWidgetItem, QMessageBox
from modules.ui_new_lab_dialog import Ui_Dialog
from PySide6.QtCore import Qt

# custom roles
ANTIBIOTIC_CODE_ROLE = Qt.UserRole + 1
ANTIBIOTIC_NAME_ROLE = Qt.UserRole + 2
ANTIBIOTIC_POTENCY_ROLE = Qt.UserRole + 3

class NewLabDialog(QDialog):
    def __init__(self):
        super(NewLabDialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.populate_country_combobox()
        self.populate_antibiotic_list()

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

        # Connecting Signals
        self.ui.general_country_combobox.currentIndexChanged.connect(self.update_country_info)
        self.ui.general_labcode_lineedit.textChanged.connect(self.update_configuration_label)
        self.ui.antibiotics_add_button.clicked.connect(self.move_antibiotic_right)
        self.ui.antibiotics_add_button.clicked.connect(self.update_num_antibiotics_label)
        self.ui.antibiotics_remove_button.clicked.connect(self.remove_antibiotic)
        self.ui.antibiotics_breakpoint_button.clicked.connect(self.list_antibiotics)
        self.ui.antibiotic_local_list.itemSelectionChanged.connect(self.update_fullname_label)
        self.ui.antibiotic_guidelines_combobox.currentIndexChanged.connect(self.update_fullname_label)
        self.ui.antibiotics_disk_radio.clicked.connect(self.update_fullname_label)
        self.ui.antibiotics_mic_radio.clicked.connect(self.update_fullname_label)
        self.ui.antibiotics_etest_radio.clicked.connect(self.update_fullname_label)
        self.ui.antibiotics_remove_button.clicked.connect(self.update_num_antibiotics_label)
        self.ui.antibiotics_remove_button.clicked.connect(self.update_fullname_label)

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
                if row[17] == "":
                    item.setData(ANTIBIOTIC_POTENCY_ROLE, 0)
                    item.setData(ANTIBIOTIC_CODE_ROLE, row[0])
                else:
                    item.setData(ANTIBIOTIC_POTENCY_ROLE, row[17])
                    potency_match = re.search(r"^\d+(?=/)", row[17])
                    if potency_match:
                        potency = potency_match.group()
                        item.setData(ANTIBIOTIC_CODE_ROLE, row[0] + potency)
                    else:
                        potency_fallback = re.search(r"\d+", row[17])
                        item.setData(ANTIBIOTIC_CODE_ROLE, row[0]+potency_fallback.group())  # Fallback if no potency value found
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
            cloned_item.setText(cloned_item.data(ANTIBIOTIC_CODE_ROLE)+"\t"+ cloned_item.data(ANTIBIOTIC_NAME_ROLE))


    def remove_antibiotic(self):
        selected_items = self.ui.antibiotic_local_list.selectedItems()
        for item in selected_items:
            self.ui.antibiotic_local_list.takeItem(self.ui.antibiotic_local_list.row(item))


    def list_antibiotics(self):
        total_antibiotics = self.ui.antibiotic_local_list.count()
        if total_antibiotics > 0:
            for i in range(total_antibiotics):
                item = self.ui.antibiotic_local_list.item(i)
                print(item.data(ANTIBIOTIC_CODE_ROLE))
                print(item.data(ANTIBIOTIC_NAME_ROLE))
                print(item.data(ANTIBIOTIC_POTENCY_ROLE))

    def update_num_antibiotics_label(self):
        num_antibiotics = self.ui.antibiotic_local_list.count()
        self.ui.num_antibiotics.setText(str(num_antibiotics))

    def update_fullname_label(self):
        if self.ui.antibiotic_local_list.currentItem() is not None:
            selected_item = self.ui.antibiotic_local_list.currentItem()
            selected_guidelines = self.ui.antibiotic_guidelines_combobox.currentText()
            if selected_guidelines == "CLSI 2023(United States)":
                selected_guidelines = "CLSI"
            else:
                selected_guidelines = "EUCAST"
            potency = selected_item.data(ANTIBIOTIC_POTENCY_ROLE)
            selected_radio = ""
            if self.ui.antibiotics_disk_radio.isChecked():
                selected_radio = "Disk"
            elif self.ui.antibiotics_mic_radio.isChecked():
                selected_radio = "MIC"
            elif self.ui.antibiotics_etest_radio.isChecked():
                selected_radio = "E-Test"

            if potency == 0:
                self.ui.antibiotics_full_name.setText(f"{selected_item.data(ANTIBIOTIC_NAME_ROLE)}_{selected_guidelines}_{selected_radio}")
            else:
                self.ui.antibiotics_full_name.setText(f"{selected_item.data(ANTIBIOTIC_NAME_ROLE)}_{selected_guidelines}_{selected_radio}_{potency}")
        else:
            self.ui.antibiotics_full_name.clear()
