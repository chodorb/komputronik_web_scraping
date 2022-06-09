from scrapy.item import Item,Field
from itemloaders.processors import TakeFirst, MapCompose
import unidecode
from w3lib.html import remove_tags
def format(value):
    return value.strip()

def format_cpu_producer(value):
    return value.strip().split(' ')[0]

def format_price(value):
    return unidecode.unidecode(value).strip().replace(' ', '')

def format_producer(value):
    return value.strip().split(' ')[0]


class Specs(Item):
    price = Field(input_processor=MapCompose(remove_tags,format_price,format), output_processor=TakeFirst())
    name = Field(input_processor=MapCompose(remove_tags,format), output_processor=TakeFirst())
    producer = Field(input_processor=MapCompose(remove_tags,format_producer,format), output_processor=TakeFirst())
    cpu_producer = Field(input_processor=MapCompose(remove_tags,format_cpu_producer,format), output_processor=TakeFirst())
    cpu = Field(input_processor=MapCompose(remove_tags,format), output_processor=TakeFirst())
    gpu = Field(input_processor=MapCompose(remove_tags,format), output_processor=TakeFirst())
    memory = Field(input_processor=MapCompose(remove_tags,format), output_processor=TakeFirst())
    drive_type = Field(input_processor=MapCompose(remove_tags,format), output_processor=TakeFirst())
    drive_capacity = Field(input_processor=MapCompose(remove_tags,format), output_processor=TakeFirst())
    mb_chipset = Field(input_processor=MapCompose(remove_tags,format), output_processor=TakeFirst())