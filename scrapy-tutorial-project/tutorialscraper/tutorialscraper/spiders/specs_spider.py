import scrapy
from scrapy.loader import ItemLoader
from tutorialscraper.items import Specs
class SpecsSpider(scrapy.Spider):
    name = 'specs'
    allowed_domains = ['komputronik.pl']
    
    start_urls = [
        "https://www.komputronik.pl/search-filter/5801/komputery-do-gier",
    ]
    
    def parse(self,response):
        for link in response.xpath('//li[@class="product-entry2 "]/div/div/a/@href').getall():
            url = response.urljoin(link)
            yield response.follow(url,callback = self.parse_specs)
            
    
    def parse_specs(self,response):
        
        loader = ItemLoader(item = Specs(),response = response)
        
        loader.add_xpath('price','//*[@id="p-inner-prices"]/div[1]/span/span')
        loader.add_xpath('name','//*[@id="p-content-specification"]/div[2]/h3')
        loader.add_xpath('producer','//*[@id="p-content-specification"]/div[2]/h3')
        loader.add_xpath('cpu_producer','//div[@class="full-specification"]/div[2]/table/tbody/tr[2]/td')
        loader.add_xpath('cpu','//div[@class="full-specification"]/div[2]/table/tbody/tr[3]/td') 
        try:
            gpu = response.xpath('//div[3]/table/tbody/tr[2]/td/text()').get().strip()
            if gpu=="":           
                gpu = response.xpath('//div[3]/table/tbody/tr[2]/td/a/text()').get().strip()
        except:
            gpu = response.xpath('//div[3]/table/tbody/tr[2]/td/a/text()').get().strip()
        loader.add_value('gpu',gpu)
        loader.add_xpath('memory','//div[@class="full-specification"]/div[4]/table/tbody/tr[1]/td/a')
        loader.add_xpath('drive_type','//div[@class="full-specification"]/div[5]/table/tbody/tr[2]/td')
        loader.add_xpath('drive_capacity','//div[@class="full-specification"]/div[5]/table/tbody/tr[2]/td')
        loader.add_xpath('mb_chipset','//div[@class="full-specification"]/div[7]/table/tbody/tr[1]/td')
        
        yield loader.load_item()