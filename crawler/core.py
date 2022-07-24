
from cgi import print_exception
import scrapy
from scrapy.http import Request
from helpers import format_price, write_to_file, encode_text
import json
   
class OlxPromowaneSpider(scrapy.Spider):
    name = 'Ogłoszenia promowane'
    start_urls = [
        'https://olx.pl',
    ]

    def start_requests(self):
        headers= {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
        for url in self.start_urls:
            yield Request(url, headers=headers)

    def parse(self, response):
        # mainpageAds = "/html/body/div[1]/section[2]/div[3]/section[2]"
        
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
            
            print('title', title)
            print("description", description)
            print("image", image)
            print("original price", price)
            print("formated_price", format_price(price))

            yield dict_list.append(
                {
                    "title" : encode_text(title),
                    "description" : description,
                    "image": image,
                    "price": format_price(price)
                }
            )

        write_to_file("output.json", dict_list)
        
        

        
            
        # for quote in response.css('div.quote'):
        #     yield {
        #         'author': quote.xpath('span/small/text()').get(),
        #         'text': quote.css('span.text::text').get(),
        #     }

        # next_page = response.css('li.next a::attr("href")').get()
        # if next_page is not None:
        #     yield response.follow(next_page, self.parse)
