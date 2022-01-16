pyinstaller -n "unzipWrapper"^
    --add-data "unzip_wrapper/ui/unzip_main.ui;./ui"^
    --add-data "../unzip_wrapper;./unzip_wrapper"^
    --add-data "../common;./common"^
    -D --clean main.py
