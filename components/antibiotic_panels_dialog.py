from PySide6.QtWidgets import QDialog, QHeaderView, QTableWidgetItem, QCheckBox, QWidget, QHBoxLayout
from modules.ui_antibiotic_panels_dialog import Ui_Dialog
from PySide6.QtCore import Qt, Signal
import pandas as pd

class AntibioticPanelsDialog(QDialog):

    dataframe_signal = Signal(str)

    def __init__(self, data, panel_state):
        super(AntibioticPanelsDialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Antibiotic Panels")
        self.setWindowFlags(self.windowFlags() | Qt.Tool)
        self.setFixedSize(1080, 720)

        self.antibiotic_data = data
        self.antibiotic_panel_data = panel_state

        # Table Logic
        organism_groups = ["Staphylococcus sp.", "Streptococcus sp.", "Streptococcus pneumoniae", "Streptococcus viridans", "Enterococcus sp.", "Gram positive urine", "Gram negative", "Gram negative urine", "Salmonella sp.", "Shigella sp.", "Pseudomonas sp.", "Non-fermenters", "Haemophilus sp.", "Campylobacter sp.", "Neisseria gonorrhoeae", "Neisseria meningitidis", "Anaerobes", "Mycobacteria", "Fungi", "Parasites"]
        self.ui.antibiotic_panel_table.setColumnCount(len(organism_groups))
        self.ui.antibiotic_panel_table.setHorizontalHeaderLabels(organism_groups)
        self.ui.antibiotic_panel_table.setRowCount(len(self.antibiotic_data))

        # Enable word wrap in horizontal header labels
        header = self.ui.antibiotic_panel_table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)
        header.setDefaultAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        
        vertical_header = []
        for row_index, row in self.antibiotic_data.iterrows():
            vertical_header.append(row['ANTIBIOTIC_FULL_NAME'])
            for col_index in range(len(organism_groups)):
                # Create a widget to hold the checkbox
                widget = QWidget()
                checkbox = QCheckBox()
                layout = QHBoxLayout(widget)
                layout.addWidget(checkbox)
                layout.setAlignment(Qt.AlignCenter)  # Center the checkbox
                layout.setContentsMargins(0, 0, 0, 0)
                widget.setLayout(layout)
                self.ui.antibiotic_panel_table.setCellWidget(row_index, col_index, widget)
        
        self.ui.antibiotic_panel_table.setVerticalHeaderLabels(vertical_header)
        self.repopulate_table()

        # Signals
        self.ui.ok_pushbutton.clicked.connect(self.accept_data)
        self.ui.cancel_pushbutton.clicked.connect(self.reject)

    def repopulate_table(self):
        # Check if the column headers match
        panel_columns = self.antibiotic_panel_data.columns
        table_columns = [self.ui.antibiotic_panel_table.horizontalHeaderItem(i).text() for i in range(self.ui.antibiotic_panel_table.columnCount())]

        # Check if the row headers match
        panel_index = self.antibiotic_panel_data.index
        table_rows = [self.ui.antibiotic_panel_table.verticalHeaderItem(i).text() for i in range(self.ui.antibiotic_panel_table.rowCount())]

        # Ensure that the data in `self.antibiotic_panel_data` is aligned with the table
        if list(panel_columns) == table_columns and list(panel_index) == table_rows:
            for row_index, row_name in enumerate(table_rows):
                for col_index, col_name in enumerate(table_columns):
                    widget = self.ui.antibiotic_panel_table.cellWidget(row_index, col_index)
                    if widget is not None:
                        checkbox = widget.findChild(QCheckBox)
                        if checkbox is not None:
                            checkbox.setChecked(self.antibiotic_panel_data.at[row_name, col_name] == 1)

    def get_checked_data(self):
        rows = self.ui.antibiotic_panel_table.rowCount()
        cols = self.ui.antibiotic_panel_table.columnCount()
        data = []

        for row in range(rows):
            row_data = []
            for col in range(cols):
                widget = self.ui.antibiotic_panel_table.cellWidget(row, col)
                if widget is not None:
                    checkbox = widget.findChild(QCheckBox)
                    if checkbox is not None and checkbox.isChecked():
                        row_data.append(1)
                    else:
                        row_data.append(0)
            data.append(row_data)

        # Retrieve horizontal header labels
        horizontal_headers = []
        for col in range(cols):
            item = self.ui.antibiotic_panel_table.horizontalHeaderItem(col)
            if item is not None:
                horizontal_headers.append(item.text())

        # Retrieve vertical header labels
        vertical_headers = []
        for row in range(rows):
            item = self.ui.antibiotic_panel_table.verticalHeaderItem(row)
            if item is not None:
                vertical_headers.append(item.text())

        # Create a DataFrame
        df = pd.DataFrame(data, columns=horizontal_headers)
        df.index = vertical_headers
        return df  

    def accept_data(self):
        self.antibiotic_panel_data = self.get_checked_data()
        print(self.antibiotic_panel_data)
        csv_data = self.antibiotic_panel_data.to_csv(index=True)
        self.dataframe_signal.emit(csv_data)
        self.accept()
