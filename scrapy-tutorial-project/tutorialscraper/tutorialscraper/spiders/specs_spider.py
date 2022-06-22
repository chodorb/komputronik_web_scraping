import scrapy
from scrapy.loader import ItemLoader
from tutorialscraper.items import Specs
from tutorialscraper.loaders import SpecsItemLoader



class SpecsSpider(scrapy.Spider):
    name = 'specs'
    allowed_domains = ['komputronik.pl']
        
    start_urls = [
        "https://www.komputronik.pl/search-filter/5801/komputery-do-gier",
    ]
    
    def parse(self, response):
        for i in range(24):
            url = f"https://www.komputronik.pl/search-filter/5801/komputery-do-gier?p={i+1}"
            yield response.follow(url,callback=self.parse_links)
    
    def parse_links(self,response):
        for link in response.xpath('//li[@class="product-entry2 "]/div/div/a/@href').getall():
            yield response.follow(link,callback = self.parse_specs)
            
    
    def parse_specs(self,response):
        
        loader = SpecsItemLoader(response=response)
        
        loader.add_xpath('price','//*[@id="p-inner-prices"]/div[@class="prices"]/span[@class="price"]/span[@class="proper"]/text()[1]')
        loader.add_xpath('name','//section[@class="p-inner-name"]/h1/text()')
        loader.add_xpath('producer','//tr[th[contains(text(),"Producent")]]/td/a/text()')
        loader.add_xpath('cpu_producer','//tr[th[contains(text(),"Typ procesora")]]/td/a/text()')
        loader.add_xpath('cpu','//tr[th[contains(text(),"Model procesora")]]/td/text()[1]') 
        try:
            gpu = response.xpath('//tr[th[contains(text(),"Karta graficzna")]]/td/text()').get().strip()
            if gpu=="":           
                gpu = response.xpath('//tr[th[contains(text(),"Karta graficzna")]]/td/a/text()').get().strip()
        except:
            gpu = response.xpath('//tr[th[contains(text(),"Karta graficzna")]]/td/a/text()').get().strip()
        loader.add_value('gpu',gpu)
        loader.add_xpath('memory','//tr[th[contains(text(),"Ilość pamięci RAM")]]/td/a/text()')
        loader.add_xpath('drive_type','//tr[th[contains(text(),"Typ dysku 1")]]/td/a/text()')
        loader.add_xpath('drive_capacity','//tr[th[contains(text(),"Pojemność dysku")]]/td/text()')
        loader.add_xpath('mb_chipset','//tr[th[contains(text(),"Chipset płyty głównej")]]/td/text()')
        
        yield loader.load_item()