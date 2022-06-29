from scrapy.loader import ItemLoader
from scrapy.loader.processors import Compose,TakeFirst,Join
from .items import Specs
from w3lib.html import remove_tags
from unidecode import unidecode

join = Join("")
join_space = Join(" ")
class SpecsItemLoader(ItemLoader):
    default_item_class = Specs
    default_input_processor = Compose(lambda value: join(value),remove_tags,lambda value: value.strip())
    default_output_processor = Compose(lambda value: join(value))
    
    price_in = Compose(lambda value: join(value),lambda value: unidecode(value),remove_tags,lambda value: value.strip())
    producer_out = Compose(lambda value: join(value),lambda value: value.split(' ')[0])     
        
    @staticmethod
    def price_out(value):
        value = join(value)
        value = value.replace(' ','')
        value = value.replace('zl','')
        value = float(value)
        return value

    @staticmethod
    def cpu_producer_out(value):
        value = join(value)
        value = remove_tags(value)
        value = value.strip()
        value = value.split(' ')[0]
        return value
    
    @staticmethod
    def drive_capacity_out(value):
        value = value[0].strip()
        return value
        