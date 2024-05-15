import sys, os
from PySide6.QtWidgets import QApplication, QMainWindow
from modules import ui_mainwindow
from components.lab_dialog import LabDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = ui_mainwindow.Ui_MainWindow()
        self.ui.setupUi(self)
        self.create_data_directory()
        self.show()
        self.showMaximized()


    def create_data_directory(self):
        data_dir = "data"
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
            print(f"Directory '{data_dir}' created.")
        else:
            print(f"Directory '{data_dir}' already exists.")


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    lab_dialog = LabDialog()
    lab_dialog.exec() 

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
