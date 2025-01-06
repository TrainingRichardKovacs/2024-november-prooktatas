'''
This module is handle file-based tasks such as open / write csv, JSON etc.

'''
import os
import json

"""
if True:
    le fog futni

if False:
    ez nem fog lefutni

not - tagadás -> not True -> False , not False -> True

"""

def get_data_from_json(file_path):
    if not os.path.exists(file_path):
       raise Exception(f"A megadott file: {file_path} nem létezik.")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    return data

def write_json(file_path, data):
    folder_path = os.path.dirname(file_path)

    if not os.path.exists(folder_path):
        raise Exception(f"A megadott útvonal: {folder_path} nem létezik.")

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    ...

    # file_path = r"C:\WORK\Prooktatas\2024-november\9_alkalom_gyak\data\data.json"

    # json_data = get_data_from_json(file_path)

    # print(json_data[0])
    # json_path = r"C:\WORK\Prooktatas\2024-november\9_alkalom_gyak\data\final_statistics\test_json.json"
    # write_json(json_path, json_data[0])

 