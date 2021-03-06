from PySide6.QtCore import QMimeData
from PySide6.QtGui import QDropEvent, QDragEnterEvent, Qt, QDragMoveEvent
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QFileSystemModel, QPushButton, QAbstractItemView, \
    QListWidget

from common.logic import user_home
from common.view import load_ui_file, get_filepath, execution_finished
from unzip_wrapper.logic import properties, unzip_archives


class DropListWidget(QListWidget):

    def __init__(self):
        super(DropListWidget, self).__init__()
        self.setDefaultDropAction(Qt.CopyAction)
        self.setDragDropMode(QAbstractItemView.DragDrop)
        self.acceptDrops()

    def dragEnterEvent(self, event: QDragEnterEvent) -> None:
        mime_data: QMimeData = event.mimeData()
        accepted: bool = False
        if mime_data.hasUrls():
            data = mime_data.urls()[0]
            file = data.toLocalFile()
            if file.endswith(".zip"):
                accepted = True
                event.acceptProposedAction()
        event.setAccepted(accepted)

    def dragMoveEvent(self, event: QDragMoveEvent) -> None:
        event.accept()

    def dropEvent(self, event: QDropEvent) -> None:
        event.setDropAction(Qt.MoveAction)
        mime_data: QMimeData = event.mimeData()
        data = mime_data.urls()[0]
        file = data.toLocalFile()
        archives = properties.archives
        if file not in archives:
            archives.append(file)
            self.addItem(file)
            event.accept()
        else:
            event.setAccepted(False)

    def clear_data(self):
        properties.archives.clear()
        self.clear()


class UnzipWrapperMainWindow(QMainWindow):

    def __init__(self, form):
        super(UnzipWrapperMainWindow, self).__init__(parent=form)
        self.adjustSize()

        form.setWindowTitle("unzipWrapper")
        form.resize(950, 600)

        self.layout = QVBoxLayout(form)

        ui_file_name = "ui/unzip_main.ui"
        ui_file = load_ui_file(ui_file_name)

        loader = QUiLoader()
        self.widget = loader.load(ui_file, form)
        ui_file.close()

        self.layout.addWidget(self.widget)

        # initialize fields
        self.tp_button: QPushButton = self.widget.tp_button  # noqa
        self.tp_edit: QLineEdit = self.widget.tp_edit  # noqa

        self.view_layout: QHBoxLayout = self.widget.view_layout  # noqa
        self.lv: DropListWidget = DropListWidget()  # noqa
        self.view_layout.addWidget(self.lv)

        self.tv: QTreeView = self.widget.tv  # noqa
        self.tv_model: QFileSystemModel = QFileSystemModel()
        self.tv_model.setNameFilters(["*.zip"])
        self.set_root_index(user_home)

        self.od_button: QPushButton = self.widget.od_button  # noqa
        self.clear_button: QPushButton = self.widget.clear_button  # noqa
        self.unzip_button: QPushButton = self.widget.unzip_button  # noqa
        self.configure_buttons()

    def set_root_index(self, directory: str):
        self.tv.setIndentation(10)
        self.tv_model.setRootPath(directory)
        self.tv.setModel(self.tv_model)
        index = self.tv_model.index(directory)
        self.tv.setRootIndex(index)

    def configure_buttons(self):
        self.tp_button.clicked.connect(self.select_target_path)
        self.od_button.clicked.connect(self.select_source_path)
        self.clear_button.clicked.connect(self.clear_list)
        self.unzip_button.clicked.connect(self.unzip_archives)

    def select_source_path(self):
        source_path = get_filepath(self, "Source directory")
        properties.source_path = source_path
        self.set_root_index(source_path)

    def select_target_path(self):
        target_path = get_filepath(self, "Target path", properties.source_path)
        self.tp_edit.setText(target_path)

    def clear_list(self):
        self.lv.clear_data()

    def unzip_archives(self):
        tp: str = self.tp_edit.text()
        if len(tp) > 0:
            properties.target_path = self.tp_edit.text()
        success: bool = unzip_archives()
        if success:
            execution_finished(self)
