
from requests import Response
import scrapy
from scrapy.http import Request
import requests
from helpers import format_price, write_to_file, get_description
from bs4 import BeautifulSoup

   
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
            link = ad.css("a::attr(href)").get()

            print("link", link)
            

            yield dict_list.append(
                {
                    "title" : title,
                    "description" : description,
                    "image": image,
                    "price": format_price(price)
                }
            )
            
            
            yield response.follow(description, callback=self.parse_description, headers=self.headers)



            

            # get_description(description, self.headers)


        write_to_file("output.json", dict_list, "json")
    
    def parse_description(self, response):
        # print()
        # css-g5mtbi-Text
        # print("response", response)
        req = requests.get(response.url)
        
        # print(html)

        soup = BeautifulSoup(req.text, 'html.parser')

        write_to_file("test.html", soup.prettify(), "html")
        # description = soup.find_all("div", {"class": "css-g5mtbi-Text"})
        # print("soup", description)
        # print("pretty", soup.prettify())
        # body = soup.body
        # description = soup.find_all(attrs={"data-cy": "ad_description"})
        # print("div", body("p", {"class":"css-g5mtbi-Text"}))
        # print("contents", body.contents)
        # print("soup", description)
        # print("contents", body.c)
        

        pass

        
        
# def parse(self, response):
#         for href in response.css('div.post-header h2 a::attr(href)').getall():
#             yield scrapy.Request(href)
#         yield scrapy.Request(
#             url=response.css('a.next-posts-link::attr(href)').get(),
#             callback=self.parse_blog_post,
#         )
#     def parse_blog_post(self, response):
#         yield {
#             'url': response.url,
#             'title': response.css('span#hs_cos_wrapper_name::text').get(),
#         }