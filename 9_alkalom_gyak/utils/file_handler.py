'''
This module is handle file-based tasks such as open / write csv, JSON etc.

'''
import json

def get_data_from_json(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    return data


if __name__ == '__main__':
    file_path = r"C:\WORK\Prooktatas\2024-november\9_alkalom_gyak\data\data.json"

    json_data = get_data_from_json(file_path)

    print(json_data[0])