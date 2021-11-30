import speech_recognition as sr


class Properties:
    file_name = ""
    input_lang = "de-DE"
    output_path = ""
    output_format = "*.txt"


properties = Properties()


def convert_file():
    speech_engine = sr.Recognizer()
    with sr.AudioFile(properties.file_name) as f:
        data = speech_engine.record(f)
        text = speech_engine.recognize_google(data, language=properties.input_lang)
        print(text)
