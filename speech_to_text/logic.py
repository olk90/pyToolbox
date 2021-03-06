import os
from pathlib import Path

import speech_recognition as sr

from common.logic import user_home


class Properties:
    file_path: str = ""
    input_lang: str = "de-DE"
    output_path: str = user_home
    output_format: str = "*.txt"


properties = Properties()


def convert_file():
    speech_engine = sr.Recognizer()
    file_path = properties.file_path
    with sr.AudioFile(file_path) as f:
        data = speech_engine.record(f)
        text = speech_engine.recognize_google(data, language=properties.input_lang)
        path = Path(file_path)
        file_name = path.stem
        output_name = os.path.join(properties.output_path, f"{file_name}.txt")
        with open(output_name, "w") as t:
            t.write(text)
