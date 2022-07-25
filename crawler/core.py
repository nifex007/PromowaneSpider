import scrapy
from scrapy.http import Request
from helpers import format_price, write_to_file

   
class OlxPromowaneSpider(scrapy.Spider):
    name = 'Ogłoszenia promowane'
    start_urls = [
        'https://olx.pl',
    ]
    headers= {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, headers=self.headers)

    
    def parse(self, response):
        mainpageAds = "//*[@id='mainpageAds']/ul/li"
        dict_list = []
        for ad in response.xpath(mainpageAds):
            a_tag = ad.xpath("./div/a")
            a_title_attribute = ad.xpath(".//@title")
            a_href_attribute = ad.xpath(".//@href")
            img_src_attribute = a_tag.xpath("./img/@src")
            title = a_title_attribute.get()
            description = a_href_attribute.get()
            
            price = ad.css(".price::text").get()
            image = img_src_attribute.get()

            yield dict_list.append(
                {
                    "title" : title,
                    "description" : description,
                    "image": image,
                    "price": format_price(price)
                }
            )
            

        write_to_file("output.json", dict_list, "json")