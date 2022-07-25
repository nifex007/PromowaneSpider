import re
from decimal import Decimal
import json
from scrapy.http import Request, Response
from bs4 import BeautifulSoup



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

def get_description(url, headers):
    # response = Request(url, headers=headers)
    # description = response.xpath("//*[@id='root']/div[1]/div[3]/div[3]/div[1]/div[2]/div[7]/div").get()
    
    # response = Response(url=url)
    # print(response.text)

    # description = response.xpath("//*[@id='root']/div[1]/div[3]/div[3]/div[1]/div[2]/div[7]/div").get()
    # print(description)

    # soup = BeautifulSoup(url, 'html.parser')
    # print("soup", soup)
    # pass
    pass



    


        

    