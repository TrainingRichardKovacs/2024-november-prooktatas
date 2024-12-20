'''
JSON - dzsézön - JavaScript Object Notation

XML

JSON érték típusok:
JSON minden kulcs " kell!

Number: a signed decimal number that may contain a fractional part and may use exponential E notation but cannot include non-numbers such as NaN. The format makes no distinction between integer and floating-point. JavaScript uses IEEE-754 double-precision floating-point format for all its numeric values (later also supporting BigInt[19]), but other languages implementing JSON may encode numbers differently.
String: a sequence of zero or more Unicode characters. Strings are delimited with double quotation marks and support a backslash escaping syntax.
Boolean: either of the values true or false
Array: an ordered list of zero or more elements, each of which may be of any type. Arrays use square bracket notation with comma-separated elements.
Object: a collection of name–value pairs where the names (also called keys) are strings. The current ECMA standard states, "The JSON syntax does not impose any restrictions on the strings used as names, does not require that name strings be unique, and does not assign any significance to the ordering of name/value pairs."[20] Objects are delimited with curly brackets and use commas to separate each pair, while within each pair, the colon ':' character separates the key or name from its value.
null: an empty value, using the word null

'''

'''
import json

file felolvasát
file kiírást

json string felolvasást
json string kiírást

'''

import json

data = [{
  "first_name": "Sámson",
  "last_name": "Karácsony",
  "is_alive": True,
  "age": 27,
  "address": {
    "street_address": "21 2nd Street",
    "city": "New York",
    "state": "NY",
    "postal_code": "10021-3100"
  },
  "phone_numbers": [
    {
      "type": "home",
      "number": "212 555-1234"
    },
    {
      "type": "office",
      "number": "646 555-4567"
    }
  ],
  "children": [
    "Catherine",
    "Thomas",
    "Trevor"
  ],
  "spouse": None
}]

file_path = r"C:\WORK\Prooktatas\2024-november\9. alkalom\test_json.json"
# dump függvény: json kiírás

# Serialization - szerzializáció: Python objectumból -> json objektumot
with open(file_path, "w", encoding="utf-8") as f_obj:
    json.dump(data, f_obj, indent=4, ensure_ascii=False)

# Deserialization - deszerializáció: JSON objektumból -> Python objectumot -> visszaalkítod
with open(file_path, "r", encoding="utf-8") as f_obj:
    json_data = json.load(f_obj)

# JSON string
json_string = json.dumps(data, indent=4, ensure_ascii=False)

# with open("test_json_from_string.json", "w", encoding="utf-8") as f:
#     f.write(json_string)

from_json_string = json.loads(json_string)

print(type(from_json_string))
print(from_json_string[0].values())