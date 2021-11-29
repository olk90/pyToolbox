import speech_recognition as sr

"""
Code template taken from https://github.com/TheMorpheus407/Python-Lets-Code/blob/master/Spracherkennung.py
"""

speech_engine = sr.Recognizer()


def from_file(file_name: str, lang: str) -> str:
    with sr.AudioFile(file_name) as f:
        data = speech_engine.record(f)
        text = speech_engine.recognize_google(data, language=lang)
        return text


def from_microphone(lang: str) -> str:
    with sr.Microphone() as micro:
        print("Recording...")
        audio = speech_engine.record(micro, duration=5)
        print("Recognition...")
        text = speech_engine.recognize_google(audio, language=lang)
        return text


class Properties:
    file_name = ""
    input_lang = "de-DE"
    output_path = ""
    output_format = "*.txt"


properties = Properties()


def foo(file_name: str):
    print(f"{file_name} --- {properties.input_lang}")
