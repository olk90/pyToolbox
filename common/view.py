import sys

from PySide6.QtCore import QFile
from PySide6.QtWidgets import QFileDialog, QWidget, QMessageBox, QMainWindow

from common.logic import user_home


def load_ui_file(filename: str) -> QFile:
    ui_file = QFile(filename)
    if not ui_file.open(QFile.ReadOnly):
        print("Cannot open {}: {}".format(filename, ui_file.errorString()))
        sys.exit(-1)
    return ui_file


def get_open_filename(parent: QWidget, caption: str, selected_filter: str) -> tuple:
    return QFileDialog.getOpenFileName(parent, caption, user_home, selected_filter)


def get_filepath(parent: QWidget, caption: str, start_dir: str = user_home) -> str:
    return QFileDialog.getExistingDirectory(parent, caption, start_dir)


def execution_finished(parent: QMainWindow):
    dlg = QMessageBox(parent)
    dlg.setWindowTitle("Information")
    dlg.setText("Execution has been completed!")
    dlg.exec()
