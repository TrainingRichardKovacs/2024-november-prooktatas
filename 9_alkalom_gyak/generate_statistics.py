from utils.file_handler import get_data_from_json
from utils.statistics import get_top_ten_expensive_data


file_path = r"C:\WORK\Prooktatas\2024-november\9_alkalom_gyak\data\data.json"

json_data = get_data_from_json(file_path)

top_ten_data = get_top_ten_expensive_data(json_data)

# print(top_ten_data)

print(top_ten_data[0])