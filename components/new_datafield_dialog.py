import csv
from PySide6.QtWidgets import QDialog , QMessageBox
from modules.ui_new_field_dialog import Ui_Dialog, QListWidgetItem
from PySide6.QtCore import Qt, Signal
import pandas as pd

FIELD_NAME_ROLE = Qt.UserRole + 1
FIELD_LENGTH_ROLE = Qt.UserRole + 2
FIELD_TYPE_ROLE = Qt.UserRole + 3
FIELD_DESCRIPTION_ROLE = Qt.UserRole + 4
FIELD_SECTION_ROLE = Qt.UserRole + 5
FIELD_ENCRYPTION_ROLE = Qt.UserRole + 6

class NewDataFieldDialog(QDialog):

    data_frame_signal = Signal(str)

    def __init__(self,data):
        super(NewDataFieldDialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Modify List")
        self.setWindowFlags(self.windowFlags() | Qt.Tool)
        self.setFixedSize(800, 600)

        self.data = data
        self.populate_selected_list()
        self.populate_alldata_list()

        # Default label values
        self.ui.datafield_description.setText("")
        self.ui.datafield_name.setText("")
        self.ui.datafield_type.setText("")
        self.ui.datafield_length_spinbox.setValue(0)

        # Signals
        self.ui.add_datafield.clicked.connect(self.add_datafield)
        self.ui.remove_datafield.clicked.connect(self.remove_datafield)
        self.ui.ok_datafield_pushbutton.clicked.connect(self.accept_data)
        self.ui.selected_datafield_list.itemSelectionChanged.connect(self.update_labels_selected)
        self.ui.all_datafield_list.itemSelectionChanged.connect(self.update_labels_all)
        self.ui.search_datafield.textChanged.connect(self.search_datafield)
        self.ui.cancel_datafield_pushbutton.clicked.connect(self.reject)

        self.original_datafield = []
        for i in range(self.ui.all_datafield_list.count()):
            item = self.ui.all_datafield_list.item(i)
            self.original_datafield.append((
                item.data(FIELD_NAME_ROLE),
                item.data(FIELD_LENGTH_ROLE),
                item.data(FIELD_TYPE_ROLE),
                item.data(FIELD_DESCRIPTION_ROLE),
                item.data(FIELD_SECTION_ROLE),
                item.data(FIELD_ENCRYPTION_ROLE)
            ))

    def search_datafield(self):
        search_text = self.ui.search_datafield.text().lower()

        self.ui.all_datafield_list.clear()

        if not search_text:
            for name, length, type, description, section, encryption in self.original_datafield:
                item = QListWidgetItem()
                item.setData(FIELD_NAME_ROLE, name)
                item.setData(FIELD_LENGTH_ROLE, length)
                item.setData(FIELD_TYPE_ROLE, type)
                item.setData(FIELD_DESCRIPTION_ROLE, description)
                item.setData(FIELD_SECTION_ROLE, section)
                item.setData(FIELD_ENCRYPTION_ROLE, encryption)
                item.setText(description)
                self.ui.all_datafield_list.addItem(item)
        else:
            filered_items = [(name, length, type, description, section, encryption) for name, length, type, description, section, encryption in self.original_datafield if description.lower().startswith(search_text)]

            for name, length, type, description, section, encryption in filered_items:
                item = QListWidgetItem()
                item.setData(FIELD_NAME_ROLE, name)
                item.setData(FIELD_LENGTH_ROLE, length)
                item.setData(FIELD_TYPE_ROLE, type)
                item.setData(FIELD_DESCRIPTION_ROLE, description)
                item.setData(FIELD_SECTION_ROLE, section)
                item.setData(FIELD_ENCRYPTION_ROLE, encryption)
                item.setText(description)
                self.ui.all_datafield_list.addItem(item)
        


    def populate_selected_list(self):
        for index, row in self.data.iterrows():
            item = QListWidgetItem()
            item.setData(FIELD_NAME_ROLE, row['FIELD_NAME'])
            item.setData(FIELD_LENGTH_ROLE, row['FIELD_LENGTH'])
            item.setData(FIELD_TYPE_ROLE, row['FIELD_TYPE'])
            item.setData(FIELD_DESCRIPTION_ROLE, row['FIELD_DESCRIPTION'])
            item.setData(FIELD_SECTION_ROLE, row['FIELD_SECTION'])
            item.setData(FIELD_ENCRYPTION_ROLE, row['FIELD_ENCRYPTION'])
            item.setText(row['FIELD_DESCRIPTION'])
            self.ui.selected_datafield_list.addItem(item)
            
    def populate_alldata_list(self):
        with open('data/FIELDLST.csv',newline="") as file:
            reader = csv.reader(file, delimiter="\t")
            next(reader)
            for row in reader:
                item = QListWidgetItem()
                item.setData(FIELD_NAME_ROLE, row[1])
                item.setData(FIELD_LENGTH_ROLE, row[2])
                item.setData(FIELD_TYPE_ROLE, row[3])
                item.setData(FIELD_DESCRIPTION_ROLE, row[0])
                item.setData(FIELD_SECTION_ROLE, row[4])
                item.setData(FIELD_ENCRYPTION_ROLE, row[7])
                item.setText(row[0])
                self.ui.all_datafield_list.addItem(item)

    def add_datafield(self):
        selected_items = self.ui.all_datafield_list.selectedItems()
    
        for item in selected_items:
            item_text = item.text()
            # Check if the item is already in the selected_datafield_list
            item_exists = False
            for i in range(self.ui.selected_datafield_list.count()):
                if self.ui.selected_datafield_list.item(i).text() == item_text:
                    item_exists = True
                    break
        
            if item_exists:
                QMessageBox.warning(self, "Warning", "Field already exists in the list")
            else:
                cloned_item = QListWidgetItem(item)
                self.ui.selected_datafield_list.addItem(cloned_item)
                self.ui.selected_datafield_list.setCurrentItem(cloned_item)
                self.ui.selected_datafield_list.scrollToItem(cloned_item)
    
    def remove_datafield(self):
        selected_items = self.ui.selected_datafield_list.selectedItems()
        for item in selected_items:
            self.ui.selected_datafield_list.takeItem(self.ui.selected_datafield_list.row(item))

    def update_labels_selected(self):
        selected_item = self.ui.selected_datafield_list.currentItem()
        if selected_item:
            self.ui.datafield_description.setText(selected_item.data(FIELD_DESCRIPTION_ROLE))
            self.ui.datafield_name.setText(selected_item.data(FIELD_NAME_ROLE))
            self.ui.datafield_type.setText(selected_item.data(FIELD_TYPE_ROLE))
            self.ui.datafield_length_spinbox.setValue(int(selected_item.data(FIELD_LENGTH_ROLE)))

    def update_labels_all(self):
        selected_item = self.ui.all_datafield_list.currentItem()
        if selected_item:
            self.ui.datafield_description.setText(selected_item.data(FIELD_DESCRIPTION_ROLE))
            self.ui.datafield_name.setText(selected_item.data(FIELD_NAME_ROLE))
            self.ui.datafield_type.setText(selected_item.data(FIELD_TYPE_ROLE))
            self.ui.datafield_length_spinbox.setValue(int(selected_item.data(FIELD_LENGTH_ROLE)))
        
        
    def accept_data(self):
        data = []
        for i in range(self.ui.selected_datafield_list.count()):
            item = self.ui.selected_datafield_list.item(i)
            data.append({
                'FIELD_NAME': item.data(FIELD_NAME_ROLE),
                'FIELD_LENGTH': item.data(FIELD_LENGTH_ROLE),
                'FIELD_TYPE': item.data(FIELD_TYPE_ROLE),
                'FIELD_DESCRIPTION': item.data(FIELD_DESCRIPTION_ROLE),
                'FIELD_SECTION': item.data(FIELD_SECTION_ROLE),
                'FIELD_ENCRYPTION': item.data(FIELD_ENCRYPTION_ROLE)
            })
        df = pd.DataFrame(data)
        csv_data = df.to_csv(index=False)

        self.data_frame_signal.emit(csv_data)
        self.accept()

