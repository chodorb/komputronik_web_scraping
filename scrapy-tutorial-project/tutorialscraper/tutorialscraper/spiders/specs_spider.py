import scrapy
import unidecode
from ..items import Specs

class SpecsSpider(scrapy.Spider):
    name = 'specs'
    allowed_domains = ['komputronik.pl']
    
    start_urls = [
        "https://www.komputronik.pl/search-filter/5801/komputery-do-gier",
    ]
    
    def parse(self,response):
        for link in response.xpath('//li[@class="product-entry2 "]/div/div/a/@href').getall():
            url = response.urljoin(link)
            yield scrapy.Request(url, callback = self.parse_specs)
    
    def parse_specs(self,response):
        
        price = response.xpath('//*[@id="p-inner-prices"]/div[1]/span/span/text()').get().strip()
        price = unidecode.unidecode(price).replace(' ','')
        
        specsentrypoint = response.xpath('//div[@class="full-specification"]')   
        name = response.xpath('//*[@id="p-content-specification"]/div[2]/h3/text()').get().strip()
        producer = name.split(' ')[0]
        cpu = specsentrypoint.xpath('//div[2]/table/tbody/tr[3]/td/text()').get().strip()
        try:
            gpu = specsentrypoint.xpath('//div[3]/table/tbody/tr[2]/td/text()').get().strip()
            if gpu=="":           
                gpu = specsentrypoint.xpath('//div[3]/table/tbody/tr[2]/td/a/text()').get().strip()
        except:
            gpu = specsentrypoint.xpath('//div[3]/table/tbody/tr[2]/td/a/text()').get().strip()
                
             
        memory = specsentrypoint.xpath('//div[4]/table/tbody/tr[1]/td/a/text()').get().strip()
        drive_type = specsentrypoint.xpath('//div[5]/table/tbody/tr[1]/td/a/text()').get().strip()
        drive_capacity = specsentrypoint.xpath('//div[5]/table/tbody/tr[2]/td/text()').get().strip()
        mb_chipset = specsentrypoint.xpath('//div[7]/table/tbody/tr[1]/td/text()').get().strip()
        
        # specs = Specs(
        #     producer=producer,
        #     price=price,
        #     name=name,
        #     cpu=cpu,
        #     memory=memory,
        #     drive_type=drive_type,
        #     drive_capacity=drive_capacity,
        #     mb_chipset=mb_chipset,
        # )
        
        # yield specs
         
        yield {
            "producer":producer,
            "price":price,
            "name":name,
            "cpu":cpu,
            "gpu":gpu,
            "memory":memory,
            "drive_type":drive_type,
            "drive_capacity":drive_capacity,
            "mb_chipset":mb_chipset
        }