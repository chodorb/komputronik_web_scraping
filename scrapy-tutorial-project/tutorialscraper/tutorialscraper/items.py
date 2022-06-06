from scrapy.item import Item,Field

class Specs(Item):
    name = Field()
    producer = Field()
    price = Field()
    cpu = Field()
    memory = Field()
    ram = Field()
    gpu = Field()
    hdd = Field()
    mb = Field()