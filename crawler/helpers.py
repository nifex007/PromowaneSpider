import re
from decimal import Decimal
import json


def format_price(raw_price: str) -> float:
    raw_price = raw_price.replace(",", ".").replace(" ", "")
    price : list = re.findall('(\d+)',  raw_price)
    price_string = ".".join(price)
    if not price or not price_string:
        return float(Decimal("0.00"))
    
    return round(float(Decimal(price_string)), 2)

def write_to_file(file_name:str, dict_list:list):
    json_data = json.dumps(dict_list, indent=4)
    
    with open(file_name, "w", encoding="utf-8") as outfile:
        outfile.write(json_data)

def encode_text(text):
    text_dump = json.dumps(text)
    text_load = json.loads(text_dump)
    return text_load.encode("UTF-8").decode("UTF-8")
    


        

    