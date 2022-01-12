from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QFileSystemModel

from common.logic import user_home
from common.view import load_ui_file, get_filepath


class UnzipWrapperMainWindow(QMainWindow):

    def __init__(self, form):
        super().__init__(parent=form)
        self.adjustSize()

        form.setWindowTitle("unzipWrapper")
        form.resize(800, 600)

        self.layout = QVBoxLayout(form)

        ui_file_name = "ui/unzip_main.ui"
        ui_file = load_ui_file(ui_file_name)

        loader = QUiLoader()
        self.widget = loader.load(ui_file, form)
        ui_file.close()

        self.layout.addWidget(self.widget)

        # initialize fields
        self.tv: QTreeView = self.widget.tv  # noqa
        self.tv_model: QFileSystemModel = QFileSystemModel()
        self.tv_model.setNameFilters(["*.zip"])
        self.setup_treeview()

        self.od_button: QPushButton = self.widget.od_button  # noqa
        self.configure_buttons()

    def setup_treeview(self):

        self.set_root_index(user_home)

        self.tv.setIndentation(10)

    def set_root_index(self, directory: str):
        self.tv_model.setRootPath(directory)
        self.tv.setModel(self.tv_model)
        index = self.tv_model.index(directory)
        self.tv.setRootIndex(index)

    def configure_buttons(self):
        self.od_button.clicked.connect(self.select_source_path)

    def select_source_path(self):
        output_path = get_filepath(self, "Source directory")
        self.set_root_index(output_path)
