from scrapy.loader import ItemLoader
from scrapy.loader.processors import Compose,TakeFirst,Join
from .items import Specs
from w3lib.html import remove_tags
from unidecode import unidecode

class SpecsItemLoader(ItemLoader):
    default_item_class = Specs
    default_input_processor = Compose(lambda value: value[0],remove_tags,lambda value: value.strip())
    default_output_processor = TakeFirst()
    
    @staticmethod
    def price_in(value):
        value = value[0]
        value = remove_tags(value)
        value = unidecode(value)
        value = value.strip()
        return value
        
    
    @staticmethod
    def price_out(value):
        value = value[0]
        value = value.replace(' ','')
        value = value.replace('zl','')
        value = float(value)
        return value

    @staticmethod
    def cpu_producer_out(value):
        value = value[0]
        value = value.split(' ')[0]
        return value
    
    @staticmethod
    def producer_in(value):
        value = value[1]
        value = remove_tags(value)
        value = value.strip()
        return value
    