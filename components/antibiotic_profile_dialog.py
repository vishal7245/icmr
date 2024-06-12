from PySide6.QtWidgets import QDialog, QTableWidgetItem, QHeaderView, QMessageBox
from modules.ui_antibiotic_profile_dialog import Ui_Dialog
from components.add_antibiotic_profile_dialog import AddAntibioticProfileDialog
from PySide6.QtCore import Qt, Signal
import pandas as pd

class AntibioticProfileDialog(QDialog):
    def __init__(self, data):
        super(AntibioticProfileDialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Antibiotic Profile")
        self.setWindowFlags(self.windowFlags() | Qt.Tool)
        self.setFixedSize(1080, 720)

        self.antibiotic_dataframe = data

        # Table Logic
        self.ui.antibiotic_profile_table.setColumnCount(2)
        self.ui.antibiotic_profile_table.verticalHeader().setVisible(False)
        self.ui.antibiotic_profile_table.setColumnWidth(0, 250)
        self.ui.antibiotic_profile_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
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



        # Signals
        self.ui.antibiotic_profile_table.cellDoubleClicked.connect(self.open_add_antibiotic_profile_dialog)
        self.ui.add_pushbutton.clicked.connect(self.add_button_clicked)
    
    def open_add_antibiotic_profile_dialog(self, row, column):
        add_profile_dialog = AddAntibioticProfileDialog(self.antibiotic_dataframe)
        add_profile_dialog.exec()



    def add_button_clicked(self):
        selected_item = self.ui.antibiotic_profile_table.selectedItems()
        if selected_item:
            row = selected_item[0].row()
            self.open_add_antibiotic_profile_dialog(row, 1)
        else:
            QMessageBox.warning(self, "Warning", "Please select an organism group to add antibiotics to.")