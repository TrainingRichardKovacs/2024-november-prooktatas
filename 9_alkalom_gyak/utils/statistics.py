"""
This module is used for analyze the data and get the necessary information from it.
"""

from uuid import uuid4


def get_top_ten_expensive_data(json_data):
    temp = {}

    for item in json_data:
        if item['price']:
            key = uuid4()

            temp[key] = {
                "phone_brand": item['phone_brand'],
                "phone_model": item['phone_model'],
                "price": get_price_value(item['price'])
            }
    # print(list(sorted(temp.items(), key=lambda item: item[1]['price'], reverse=True))[0:11])
   
    sorted_data = sorted(temp.items(), key=lambda item: item[1]['price'], reverse=True)
    list_sorted_data = list(sorted_data)
    return list_sorted_data[0:11], temp   
    

def get_price_value(price: str):
    retval = 'Karcsi'

    if all(x in price for x in ['About', 'EUR']):
        retval = int(price.replace('About', '').replace('EUR', ''))
    elif all(x in price for x in ['About', 'INR']):
        retval = get_eur_value_of_price(['₹', price.replace('About', '').replace('INR', '')])        
    elif all(x in price for x in ['About', 'BTC']):
        retval = get_eur_value_of_price(['BTC', float(price.replace('About', '').replace('BTC', '').split('/')[0])])
    elif all(x in price for x in ['\u2009']) and '/' not in price:
        retval = get_eur_value_of_price(price.split('\u2009'))

    elif all(x in price for x in ['\u2009']) and '/' in price:
        retval = get_eur_value_of_price(price.split()[0:2])
    else:
        temp = price.split(' ')
        print("Valamilyen eltérő currency")

    return retval


def get_eur_value_of_price(price):
    retval = None

    if price[0] == 'BTC':
        retval = float(price[1]) * 98167
    elif price[0] == '$':
        retval = float(price[1].replace(',', '')) * 0.97
    elif price[0] == '£':
        retval = float(price[1].replace(',', '')) * 1.21
    elif price[0] == '₹':
        retval = float(price[1].replace(',', '')) * 0.011
    elif price[0] == '€':
        retval = float(price[1].replace(',', ''))
    elif price[0] == 'C$':
        retval = float(price[1].replace(',', '')) * 0.67
    elif price[0] == 'A$':
        retval = float(price[1].replace(',', '')) * 0.60
    else:
        print(f"hiba van a price-al: {price}")

    return retval

def get_brand_value(cleaned_data: list, nth_top=5):
    """
    Set data type: olyan adattípus, amiben nincs ismétlődés
    A set egy mutable adattípus -> lehet elemet hozzáadni, elvenni, módosítani

    A set-nél tudjuk használni a matematikai halmazműveleteket
    Don’t forget that set elements must be immutable

    my_set = {10, 20, 30, 40, 50}
    
    """
    top_brands = {}
    min_max_brands = {}
    for item in cleaned_data:
        brand = item[1]['phone_brand']
        if not top_brands.get(brand):
            top_brands[brand] = 0            
            min_max_brands[brand] = { "phone_model_type": set() }

        top_brands[brand] += item[1]['price']

        min_max_brands[brand]['phone_model_type'].add(item[1]['phone_model'])

    sorted_data = sorted(top_brands.items(), key=lambda item: item[1], reverse=True)
    list_sorted_data = list(sorted_data)
    
    min_max_final_dict = {}

    min_value = {
        "brand": None,
        "value": 0
    }
    max_value = {
        "brand": None,
        "value": 0
    }

    for idx, item in enumerate(min_max_brands.items()):
        if idx == 0:
            min_value = {
                "brand": item[0],
                "value": len(item[1]['phone_model_type'])
            }
            continue

        if min_value['value'] > len(item[1]['phone_model_type']):
            min_value = {
                "brand": item[0],
                "value": len(item[1]['phone_model_type'])
            }
        
        if max_value['value'] < len(item[1]['phone_model_type']):
            max_value = {
                "brand": item[0],
                "value": len(item[1]['phone_model_type'])
            }
        

    min_max_final_dict = {
       "max_value": max_value,
       "min_value": min_value
    }

    min_sorted = sorted(min_max_brands.items(), key=lambda item: len(item[1]['phone_model_type']), reverse=True)
    list_min_sorted = list(min_sorted)

    min_max_final_dict = {
       "max_value": {
           list_min_sorted[0][0]: len(list_min_sorted[0][1]['phone_model_type'])
                     },
       "min_value": {
           list_min_sorted[-1][0]: len(list_min_sorted[-1][1]['phone_model_type'])
                     }
    }

    # innen folytatjuk
    print(min_max_final_dict)

    return list_sorted_data[0:nth_top+1]

if __name__ == '__main__':
    
    # full-path -> C:\WORK\Prooktatas\2024-november\9_alkalom_gyak\utils\statistics.py
    # relative-path -> ./file_handler
    import sys
    sys.path.append(r"C:\WORK\Prooktatas\2024-november\9_alkalom_gyak")
    from utils.file_handler import get_data_from_json

    file_path = r"C:\WORK\Prooktatas\2024-november\9_alkalom_gyak\data\data.json"
    json_data = get_data_from_json(file_path)

    top_ten_data = get_top_ten_expensive_data(json_data)
    
    # print(top_ten_data[0])
    # temp = [item for item in top_ten_data[1].items()]
    temp = list(top_ten_data[1].items())

    top_brand_value = get_brand_value(temp, 10)

    print(top_brand_value)
