#!/bin/zsh
pyinstaller -n "unzipWrapper" \
  --add-data "ui/unzip_main.ui:./ui" \
  --add-data "../unzip_wrapper:./unzip_wrapper" \
  --add-data "../common:./common" \
  -D --clean main.py
