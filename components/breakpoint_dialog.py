import csv
import re
from PySide6.QtWidgets import QDialog, QHeaderView, QTableWidgetItem
from modules.ui_breakpoint_dialog import Ui_Dialog
import pandas as pd

class BreakpointDialog(QDialog):
    def __init__(self, data):
        super(BreakpointDialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Breakpoints")
        self.data = data
        self.breakpoint_data = self.fetch_breakpoints()

        # ComboBox
        self.ui.breakpoint_organism_combobox.addItem("All")
        self.ui.breakpoint_organism_combobox.addItems(self.breakpoint_data['ORGANISM'].unique())
        self.ui.breakpoint_siteofinfection_combobox.addItem("All")
        self.ui.breakpoint_siteofinfection_combobox.addItems(self.breakpoint_data['SITE_OF_INFECTION'].unique())
        self.ui.breakpoint_antibiotic_combobox.addItem("All")
        self.ui.breakpoint_antibiotic_combobox.addItems(self.breakpoint_data['ANTIBIOTIC_FULL_NAME'].unique())
        self.ui.breakpoint_testmethod_combobox.addItem("All")
        self.ui.breakpoint_testmethod_combobox.addItems(self.breakpoint_data['TEST'].unique())
        self.ui.breakpoint_type_combobox.addItem("All")
        self.ui.breakpoint_type_combobox.addItems(self.breakpoint_data['BREAKPOINT_TYPE'].unique())

        # ComboBox Signals
        self.ui.breakpoint_organism_combobox.currentIndexChanged.connect(self.filter_breakpoint_table)
        self.ui.breakpoint_siteofinfection_combobox.currentIndexChanged.connect(self.filter_breakpoint_table)
        self.ui.breakpoint_antibiotic_combobox.currentIndexChanged.connect(self.filter_breakpoint_table)
        self.ui.breakpoint_testmethod_combobox.currentIndexChanged.connect(self.filter_breakpoint_table)
        self.ui.breakpoint_type_combobox.currentIndexChanged.connect(self.filter_breakpoint_table)

        # Breakpoint table setup
        self.ui.breakpoint_table.setColumnCount(10)
        self.ui.breakpoint_table.setHorizontalHeaderLabels([
            "Organism", "Code", "Site of Infection", "Breakpoint type",
            "Host", "Antibiotic", "Test", "R<=", "I", "S>="
        ])
        self.ui.breakpoint_table.verticalHeader().setVisible(False)

        # Set column widths
        column_widths = [250, 50, 150, 110, 100, 250, 50, 50, 50, 50]
        for i, width in enumerate(column_widths):
            self.ui.breakpoint_table.setColumnWidth(i, width)

        # Populate table with initial data
        self.populate_breakpoint_table(self.breakpoint_data)

    def fetch_breakpoints(self):
        ANTIBIOTIC_CODE = []
        ORGANISM_CODE = []
        ORGANISM = []
        BREAKPOINT_TYPE = []
        HOST = []
        SITE_OF_INFECTION = []
        ANTIBIOTIC_FULL_NAME = []
        TEST = []
        R = []
        I = []
        S = []

        for index, row in self.data.iterrows():
            UPDATED_ANTIBIOTIC_CODES = re.match(r'^([^_]+)', row['ANTIBIOTIC_CODES']).group(1)
            with open("data/Breakpoints_updated.csv", newline="") as breakpointcsv:
                reader = csv.reader(breakpointcsv, delimiter=',')
                for roww in reader:
                    if (UPDATED_ANTIBIOTIC_CODES == roww[12] and
                        row['ANTIBIOTIC_GUIDELINES'] == roww[0] and
                        row['ANTIBIOTIC_TEST'].upper() == roww[2]):
                        ANTIBIOTIC_CODE.append(self.safe_value(row['ANTIBIOTIC_CODES']))
                        ANTIBIOTIC_FULL_NAME.append(self.safe_value(row['ANTIBIOTIC_FULL_NAME']))
                        TEST.append(self.safe_value(row['ANTIBIOTIC_TEST']))
                        ORGANISM_CODE.append(self.safe_value(roww[5]))
                        BREAKPOINT_TYPE.append(self.safe_value(roww[7]))
                        HOST.append(self.safe_value(roww[8]))
                        SITE_OF_INFECTION.append(self.safe_value(roww[9]))
                        ORGANISM.append(self.safe_value(roww[4]))
                        R.append(self.safe_value(roww[14]))
                        I.append(self.safe_value(roww[15]))
                        S.append(self.safe_value(roww[17]))

        data = {
            "ANTIBIOTIC_CODE": ANTIBIOTIC_CODE,
            "ANTIBIOTIC_FULL_NAME": ANTIBIOTIC_FULL_NAME,
            "TEST": TEST,
            "ORGANISM_CODE": ORGANISM_CODE,
            "BREAKPOINT_TYPE": BREAKPOINT_TYPE,
            "HOST": HOST,
            "SITE_OF_INFECTION": SITE_OF_INFECTION,
            "ORGANISM": ORGANISM,
            "R": R,
            "I": I,
            "S": S
        }

        df = pd.DataFrame(data)
        return df

    def safe_value(self, value):
        return value if value is not None and value != "" else ""

    def populate_breakpoint_table(self, data):
        self.ui.breakpoint_table.setRowCount(0)  # Clear existing rows
        for index, row in data.iterrows():
            self.ui.breakpoint_table.insertRow(index)
            self.ui.breakpoint_table.setItem(index, 0, self.create_table_item(row['ORGANISM']))
            self.ui.breakpoint_table.setItem(index, 1, self.create_table_item(row['ORGANISM_CODE']))
            self.ui.breakpoint_table.setItem(index, 2, self.create_table_item(row['SITE_OF_INFECTION']))
            self.ui.breakpoint_table.setItem(index, 3, self.create_table_item(row['BREAKPOINT_TYPE']))
            self.ui.breakpoint_table.setItem(index, 4, self.create_table_item(row['HOST']))
            self.ui.breakpoint_table.setItem(index, 5, self.create_table_item(row['ANTIBIOTIC_FULL_NAME']))
            self.ui.breakpoint_table.setItem(index, 6, self.create_table_item(row['TEST']))
            self.ui.breakpoint_table.setItem(index, 7, self.create_table_item(row['R']))
            self.ui.breakpoint_table.setItem(index, 8, self.create_table_item(row['I']))
            self.ui.breakpoint_table.setItem(index, 9, self.create_table_item(row['S']))

    def create_table_item(self, text):
        item = QTableWidgetItem(str(text))
        return item

    def filter_breakpoint_table(self):
        organism = self.ui.breakpoint_organism_combobox.currentText()
        site_of_infection = self.ui.breakpoint_siteofinfection_combobox.currentText()
        antibiotic = self.ui.breakpoint_antibiotic_combobox.currentText()
        test_method = self.ui.breakpoint_testmethod_combobox.currentText()
        breakpoint_type = self.ui.breakpoint_type_combobox.currentText()
        filtered_data = self.breakpoint_data
        if organism != "All":
            filtered_data = self.breakpoint_data[self.breakpoint_data['ORGANISM'] == organism].reset_index(drop=True)
        if site_of_infection != "All":
            filtered_data = filtered_data[filtered_data['SITE_OF_INFECTION'] == site_of_infection].reset_index(drop=True)
        if antibiotic != "All":
            filtered_data = filtered_data[filtered_data['ANTIBIOTIC_FULL_NAME'] == antibiotic].reset_index(drop=True)
        if test_method != "All":
            filtered_data = filtered_data[filtered_data['TEST'] == test_method].reset_index(drop=True)
        if breakpoint_type != "All":
            filtered_data = filtered_data[filtered_data['BREAKPOINT_TYPE'] == breakpoint_type].reset_index(drop=True)
        self.populate_breakpoint_table(filtered_data)
