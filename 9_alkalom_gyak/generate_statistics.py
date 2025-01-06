from utils.file_handler import get_data_from_json
from utils import statistics


file_path = r"C:\WORK\Prooktatas\2024-november\9_alkalom_gyak\data\data.json"

json_data = get_data_from_json(file_path)

print(json_data[0])