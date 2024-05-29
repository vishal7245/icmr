import sys, sqlite3
from PySide6.QtWidgets import QDialog, QAbstractItemView, QHeaderView, QTableWidgetItem
from PySide6.QtCore import Qt
from .new_lab_dialog import NewLabDialog

# Add the parent directory to sys.path
sys.path.append('../')

from modules.ui_lab_dialog import Ui_Dialog

class LabDialog(QDialog):
    def __init__(self):
        super(LabDialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Laboratories")
        self.ui.tableWidget.setColumnCount(4)
        self.ui.tableWidget.setHorizontalHeaderLabels(["Country Code", "Laboratory Code","File Name","Lab Name"])
        self.ui.tableWidget.verticalHeader().setVisible(False)
        self.ui.tableWidget.setShowGrid(False)
        self.ui.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        header = self.ui.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.Stretch)
        header.setSectionResizeMode(3, QHeaderView.Stretch)
        self.populate_table()

        # self.ui.browse_button.clicked.connect(self.print_selected_row)
        self.ui.new_laboratory.clicked.connect(self.open_new_lab_dialog)

        self.setFixedSize(800,600)

    def populate_table(self):
        conn = sqlite3.connect("data/init_db.sqlite")
        cursor = conn.cursor()

        cursor.execute('''SELECT * FROM Labs''')
        data = cursor.fetchall()

        self.ui.tableWidget.setRowCount(len(data)) 

        for index, row in enumerate(data):

            country_code = QTableWidgetItem(row[0])
            country_code.setFlags(country_code.flags() & ~Qt.ItemIsEditable)  # Make item uneditable
            laboratory_code = QTableWidgetItem(row[1])
            laboratory_code.setFlags(laboratory_code.flags() & ~Qt.ItemIsEditable)
            file_name = QTableWidgetItem(row[2])
            file_name.setFlags(file_name.flags() & ~Qt.ItemIsEditable)
            laboratory_name = QTableWidgetItem(row[3])
            laboratory_name.setFlags(laboratory_name.flags() & ~Qt.ItemIsEditable)

            self.ui.tableWidget.setItem(index, 0, country_code)
            self.ui.tableWidget.setItem(index, 1, laboratory_code)
            self.ui.tableWidget.setItem(index, 2, file_name)
            self.ui.tableWidget.setItem(index, 3, laboratory_name)


        conn.close()

    # def print_selected_row(self):
    #     selected_row = self.ui.tableWidget.currentRow()
    #     if selected_row >= 0:
    #         row_data = []
    #         for column in range(self.ui.tableWidget.columnCount()):
    #             item = self.ui.tableWidget.item(selected_row, column)
    #             row_data.append(item.text())
    #         print("Selected Row Data:", row_data)
    #     else:
    #         print("No row selected.")


    def open_new_lab_dialog(self):
        new_lab_dialog = NewLabDialog()
        new_lab_dialog.exec()