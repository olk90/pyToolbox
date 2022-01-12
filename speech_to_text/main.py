import sys

from PySide6 import QtCore
from PySide6.QtWidgets import QApplication, QWidget
from view import PySSTMainWindow

if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)

    app = QApplication()
    form = QWidget(None)
    PySSTMainWindow(form)

    form.show()
    sys.exit(app.exec())
