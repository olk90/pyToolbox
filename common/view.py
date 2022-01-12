import sys

from PySide6.QtCore import QFile


def load_ui_file(filename: str) -> QFile:
    ui_file = QFile(filename)
    if not ui_file.open(QFile.ReadOnly):
        print("Cannot open {}: {}".format(filename, ui_file.errorString()))
        sys.exit(-1)
    return ui_file
