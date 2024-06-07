import csv
from PySide6.QtWidgets import QDialog, QHeaderView, QTableWidgetItem, QCheckBox, QWidget, QHBoxLayout
from modules.ui_encryption_dialog import Ui_Dialog
import pandas as pd
from PySide6.QtCore import Qt, Signal

class EncryptionDialog(QDialog):

    data_frame_signal = Signal(str)

    def __init__(self, data):
        super(EncryptionDialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Encryption")
        self.setWindowFlags(self.windowFlags() | Qt.Tool)
        self.setFixedSize(800, 600)
        self.datafield_df = data

        self.ui.encryption_table.setColumnCount(2)
        self.ui.encryption_table.setHorizontalHeaderLabels(["Data Field", "Encryption"])
        self.ui.encryption_table.verticalHeader().setVisible(False)

        header = self.ui.encryption_table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        self.populate_encryption_list()

        # Signals
        self.ui.ok_button.clicked.connect(self.accept_data)
        self.ui.cancel_button.clicked.connect(self.reject)

    def populate_encryption_list(self):
        for index, row in self.datafield_df.iterrows():
            # Insert a new row in the table
            self.ui.encryption_table.insertRow(index)
            # Create and set the description item (non-editable)
            data_field = QTableWidgetItem(row['FIELD_DESCRIPTION'])
            data_field.setFlags(data_field.flags() & ~Qt.ItemIsEditable)
            self.ui.encryption_table.setItem(index, 0, data_field)
        
            # Create and set the checkbox for encryption status
            checkbox = QCheckBox()
            if int(row['FIELD_ENCRYPTION']) == 1:
                checkbox.setChecked(True)
        
            # Center the checkbox in the cell
            checkbox_widget = QWidget()
            layout = QHBoxLayout(checkbox_widget)
            layout.addWidget(checkbox)
            layout.setAlignment(checkbox, Qt.AlignCenter)
            layout.setContentsMargins(0, 0, 0, 0)
            self.ui.encryption_table.setCellWidget(index, 1, checkbox_widget)
    
    def convert_into_dataframe(self):
        for index in range(self.ui.encryption_table.rowCount()):
            checkbox = self.ui.encryption_table.cellWidget(index, 1).layout().itemAt(0).widget()
            if checkbox.isChecked():
                self.datafield_df.loc[index, 'FIELD_ENCRYPTION'] = 1
            else:
                self.datafield_df.loc[index, 'FIELD_ENCRYPTION'] = 0
        return self.datafield_df

    def accept_data(self):
        data_frame = self.convert_into_dataframe()
        csv_data = data_frame.to_csv(index=False)
        self.data_frame_signal.emit(csv_data)
        self.accept()
    

    
