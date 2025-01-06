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
    
    

def get_price_value(price: str):
    retval = None

    if all(x in price for x in ['About', 'EUR']):
        retval = int(price.replace('About', '').replace('EUR', ''))
    elif all(x in price for x in ['About', 'INR']):
        retval = get_eur_value_of_price(['₹', price.replace('About', '').replace('INR', '')])        
    elif all(x in price for x in ['About', 'BTC']):
        retval = get_eur_value_of_price(['BTC', float(price.replace('About', '').replace('BTC', '').split('/')[0])])
    elif all(x in price for x in ['\u2009']) and '/' not in price:
        retval = get_eur_value_of_price(price.split('\u2009'))

    elif all(x in price for x in ['\u2009']) and '/' in price:
        get_eur_value_of_price(price.split()[0:2])
    else:
        temp = price.split(' ')
        print(price)

    return retval


def get_eur_value_of_price(price):
    retval = None

    if price[0] == 'BTC':
        retval = price * 98167
    elif price[0] == '$':
        retval = float(price[1].replace(',', '')) * 1.04
    elif price[0] == '£':
        retval = float(price[1].replace(',', '')) * 1.21
    elif price[0] == '₹':
        retval = float(price[1].replace(',', '')) * 88.99
    elif price[0] == '€':
        retval = float(price[1].replace(',', ''))
    elif price[0] == 'C$':
        retval = float(price[1].replace(',', '')) * 1.49
    elif price[0] == 'A$':
        retval = float(price[1].replace(',', '')) * 1.66
    else:
        print(price)

    return retval

if __name__ == '__main__':
    
    # full-path -> C:\WORK\Prooktatas\2024-november\9_alkalom_gyak\utils\statistics.py
    # relative-path -> ./file_handler
    import sys
    sys.path.append(r"C:\WORK\Prooktatas\2024-november\9_alkalom_gyak")
    from utils.file_handler import get_data_from_json

    file_path = r"C:\WORK\Prooktatas\2024-november\9_alkalom_gyak\data\data.json"
    json_data = get_data_from_json(file_path)

    get_top_ten_expensive_data(json_data)
    