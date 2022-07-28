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

def write_to_file(file_name:str, doc, format="json"):
    if format=="json":
        doc = json.dumps(doc, indent=4)
    
    with open(file_name, "w", encoding="utf-8") as outfile:
        outfile.write(doc)
    
