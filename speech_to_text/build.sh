#!/bin/zsh
pyinstaller -n "pySTT" \
  --add-data "ui/pystt_main.ui:./ui" \
  --add-data "../speech_to_text:./speech_to_text" \
  --add-data "../common:./common" \
  -D --clean main.py
