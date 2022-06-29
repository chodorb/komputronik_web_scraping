import scrapy
from scrapy.loader import ItemLoader
from tutorialscraper.items import Specs
from tutorialscraper.loaders import SpecsItemLoader
from tutorialscraper.utils import specs_table_xpath,specs_table_link_xpath


class SpecsSpider(scrapy.Spider):
    name = 'specs'
    allowed_domains = ['komputronik.pl']
        
    start_urls = [
        "https://www.komputronik.pl/search-filter/5801/komputery-do-gier",
    ]
    
    def parse(self, response):
        r = int(response.xpath('//div[@class="pagination text-xs-center text-lg-right text-md-right isp-top-10"]/ul/li[last()-1]/a/text()').get())
        for i in range(r):
            url = f"https://www.komputronik.pl/search-filter/5801/komputery-do-gier?p={i+1}"
            yield response.follow(url,callback=self.parse_links)
    
    def parse_links(self,response):
        for link in response.xpath('//li[@class="product-entry2 "]/div/div/a/@href').getall():
            yield response.follow(link,callback = self.parse_specs)
            
    
    def parse_specs(self,response):
        
        loader = SpecsItemLoader(response=response)
        
        loader.add_xpath('price','//*[@id="p-inner-prices"]/div[@class="prices"]/span[@class="price"]/span[@class="proper"]/text()[1]')
        loader.add_xpath('name','//section[@class="p-inner-name"]/h1/text()')
        loader.add_xpath('producer','//section[@class="p-inner-name"]/h1/text()')
        loader.add_xpath('cpu_producer',specs_table_link_xpath('Typ procesora'))
        loader.add_xpath('cpu',specs_table_xpath('Model procesora')) 
        loader.add_xpath('gpu',[specs_table_link_xpath('Karta graficzna'),specs_table_xpath('Karta graficzna')])
        loader.add_xpath('memory',specs_table_link_xpath('Ilość pamięci RAM'))
        loader.add_xpath('drive_type',specs_table_link_xpath('Typ dysku 1'))
        loader.add_xpath('drive_capacity',specs_table_xpath('Pojemność dysku'))
        loader.add_xpath('mb_chipset',specs_table_xpath('Chipset płyty głównej'))
        
        yield loader.load_item()