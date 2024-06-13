from PySide6.QtWidgets import QDialog, QTableWidgetItem, QHeaderView, QMessageBox, QAbstractItemView
from modules.ui_antibiotic_profile_dialog import Ui_Dialog
from components.add_antibiotic_profile_dialog import AddAntibioticProfileDialog
from PySide6.QtCore import Qt, Signal
import pandas as pd
from io import StringIO

class AntibioticProfileDialog(QDialog):

    dataframe_signal = Signal(str)
    def __init__(self, data, profile_state):
        super(AntibioticProfileDialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Antibiotic Profile")
        self.setWindowFlags(self.windowFlags() | Qt.Tool)
        self.setFixedSize(1080, 720)

        self.antibiotic_dataframe = data
        self.selected_antibiotic_dataframe = profile_state

        # Table Logic
        self.ui.antibiotic_profile_table.setColumnCount(2)
        self.ui.antibiotic_profile_table.verticalHeader().setVisible(False)
        self.ui.antibiotic_profile_table.setColumnWidth(0, 250)
        self.ui.antibiotic_profile_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.ui.antibiotic_profile_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.ui.antibiotic_profile_table.setHorizontalHeaderLabels(["Organism Groups", "Antibiotics"])
        organism_groups = ["Staphylococcus sp.", "Streptococcus sp.", "Streptococcus pneumoniae", "Streptococcus viridans", "Enterococcus sp.", "Gram positive urine", "Gram negative", "Gram negative urine", "Salmonella sp.", "Shigella sp.", "Pseudomonas sp.", "Non-fermenters", "Haemophilus sp.", "Campylobacter sp.", "Neisseria gonorrhoeae", "Neisseria meningitidis", "Anaerobes", "Mycobacteria", "Fungi", "Parasites"]
        self.ui.antibiotic_profile_table.setRowCount(len(organism_groups))
        for i, organism_group in enumerate(organism_groups):
            item = QTableWidgetItem(organism_group)
            item.setFlags(item.flags() & ~Qt.ItemIsEditable & ~Qt.ItemIsSelectable)
            self.ui.antibiotic_profile_table.setItem(i, 0, item)
            item = QTableWidgetItem()
            item.setFlags(item.flags() & ~Qt.ItemIsEditable)
            self.ui.antibiotic_profile_table.setItem(i, 1, item)

        self.repopulate_table()

        # Signals
        self.ui.antibiotic_profile_table.cellDoubleClicked.connect(self.open_add_antibiotic_profile_dialog)
        self.ui.add_pushbutton.clicked.connect(self.add_button_clicked)
        self.ui.edit_pushbutton.clicked.connect(self.edit_profile)
        self.ui.ok_pushbutton.clicked.connect(self.accept_data)
        self.ui.cancel_pushbutton.clicked.connect(self.reject)
    
    def repopulate_table(self):
        for index, row in self.selected_antibiotic_dataframe.iterrows():
            item = QTableWidgetItem(row['Antibiotics'])
            item.setFlags(item.flags() & ~Qt.ItemIsEditable)
            self.ui.antibiotic_profile_table.setItem(index, 1, item)

    def open_add_antibiotic_profile_dialog(self, row, column):
        row_data = self.ui.antibiotic_profile_table.item(row, column).text()
        add_profile_dialog = AddAntibioticProfileDialog(self.antibiotic_dataframe, row, column, row_data)
        add_profile_dialog.profile_signal.connect(self.handle_new_profile_data)
        add_profile_dialog.exec()

    def edit_profile(self):
        selected_item = self.ui.antibiotic_profile_table.selectedItems()
        if selected_item[0].text():
            row = selected_item[0].row()
            column = selected_item[0].column()
            row_data = self.ui.antibiotic_profile_table.item(row, column).text()
            add_profile_dialog = AddAntibioticProfileDialog(self.antibiotic_dataframe, row, column, row_data)
            add_profile_dialog.profile_signal.connect(self.handle_new_profile_data)
            add_profile_dialog.exec()
        else:
            QMessageBox.warning(self, "Warning", "Please select an organism group to edit antibiotics.")

    def handle_new_profile_data(self, profile_data, supplement_data,table_row, column):
        column = 1
        profile_df = pd.read_csv(StringIO(profile_data))
        if supplement_data == "None":
            final_list = []
            for index, row in profile_df.iterrows():
                final_list.append(row['ANTIBIOTIC_CODE'])
            final_string = ",".join(final_list)
        else:
            supplement_df = pd.read_csv(StringIO(supplement_data))
            profile_list = []
            supplement_list = []
            for index, row in profile_df.iterrows():
                profile_list.append(row['ANTIBIOTIC_CODE'])
            for index, row in supplement_df.iterrows():
                supplement_list.append(row['ANTIBIOTIC_CODE'])
            final_string = ",".join(profile_list) + " (" + ",".join(supplement_list) + ")"
        item = QTableWidgetItem(final_string)
        item.setFlags(item.flags() & ~Qt.ItemIsEditable)
        self.ui.antibiotic_profile_table.setItem(table_row, column, item)
            
        # create profile table dataframe
        profile_table_df = pd.DataFrame(columns=["Organism Groups", "Antibiotics"])
        organism_groups = ["Staphylococcus sp.", "Streptococcus sp.", "Streptococcus pneumoniae", "Streptococcus viridans", "Enterococcus sp.", "Gram positive urine", "Gram negative", "Gram negative urine", "Salmonella sp.", "Shigella sp.", "Pseudomonas sp.", "Non-fermenters", "Haemophilus sp.", "Campylobacter sp.", "Neisseria gonorrhoeae", "Neisseria meningitidis", "Anaerobes", "Mycobacteria", "Fungi", "Parasites"]
        for i, organism_group in enumerate(organism_groups):
            item = self.ui.antibiotic_profile_table.item(i, 1)
            if item is not None:  # Check if item is not None
                antibiotics = item.text()
            else:
                antibiotics = None
            profile_table_df.loc[i] = {"Organism Groups": organism_group, "Antibiotics": antibiotics}

        self.selected_antibiotic_dataframe = profile_table_df        
        

    def add_button_clicked(self):
        selected_item = self.ui.antibiotic_profile_table.selectedItems()
        if selected_item:
            row = selected_item[0].row()
            self.open_add_antibiotic_profile_dialog(row, 1)
        else:
            QMessageBox.warning(self, "Warning", "Please select an organism group to add antibiotics to.")


    def accept_data(self):
        csv_data = self.selected_antibiotic_dataframe.to_csv(index=False)
        self.dataframe_signal.emit(csv_data)
        self.accept()
