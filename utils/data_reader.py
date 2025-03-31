import json
from enum import Enum
import os

class LanguageFile(Enum):
    en          = "English"
    ja          = "Japanese"

class FileLoader:
    @staticmethod
    def load_languages(folder_path : str):
        json_filename_list = [f for f in os.listdir(folder_path) if f.endswith(".json")]
        languages = [LanguageFile[f.replace(".json","")].value for f in json_filename_list]
        return languages

    @staticmethod
    def load_file_path(folder_path : str,language : str):
        return os.path.join(folder_path,LanguageFile(language).name + ".json")

    @staticmethod
    def load_json(filepath : str):
        """Đọc dữ liệu từ file JSON và trả về dictionary."""
        with open(filepath, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data