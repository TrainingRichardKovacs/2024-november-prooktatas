# from utils.file_handler import get_data_from_json, write_json
# from utils.statistics import get_top_ten_expensive_data, get_brand_value, get_os_data

from utils import (get_data_from_json,
                   write_json,
                   get_top_ten_expensive_data,
                   get_brand_value,
                   get_os_data)

# CONSTANST VÁLTOZÓK
FILE_PATH = r"C:\WORK\Prooktatas\2024-november\9_alkalom_gyak\data\data.json"
STATISTICS_FOLDER = r"C:\WORK\Prooktatas\2024-november\9_alkalom_gyak\data\final_statistics"

def main():
    json_data = get_data_from_json(FILE_PATH)
    top_ten_data, temp = get_top_ten_expensive_data(json_data)

    temp = list(temp.items())
    top_brand_value = get_brand_value(temp, 15)

    os_data = get_os_data(json_data)

    top_ten_file_name = f"{STATISTICS_FOLDER}/top_ten_brand.json"
    write_json(top_ten_file_name, top_ten_data)

    top_brands_file_name = f"{STATISTICS_FOLDER}/top_brands_value.json"
    write_json(top_brands_file_name, top_brand_value)

    os_file_name = f"{STATISTICS_FOLDER}/os_statistics.json"
    write_json(os_file_name, [os_data])


if __name__ == '__main__':
    main()
