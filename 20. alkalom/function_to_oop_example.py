import os
import json

class FileHandler:

    def __init__(self, file_path):
        self.file_path = file_path

    def get_data_from_json(self):
        if not os.path.exists(self.file_path):
            raise Exception(f"A megadott file: {self.file_path} nem létezik.")

        with open(self.file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        return data

    @staticmethod
    def write_json(json_path, data):
        folder_path = os.path.dirname(json_path)

        if not os.path.exists(folder_path):
            raise Exception(f"A megadott útvonal: {folder_path} nem létezik.")

        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    
    file_path = r"C:\WORK\Prooktatas\2024-november\9_alkalom_gyak\data\data.json"

    file_handler = FileHandler(file_path=file_path)

    json_data = file_handler.get_data_from_json()

    print(json_data[0])
    json_path = r"C:\WORK\Prooktatas\2024-november\9_alkalom_gyak\data\final_statistics\test_json.json"
    file_handler.write_json(json_path, json_data[0])