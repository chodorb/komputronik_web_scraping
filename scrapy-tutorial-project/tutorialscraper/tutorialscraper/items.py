from scrapy.item import Item,Field



class Specs(Item):
    price = Field()
    name = Field()
    producer = Field()
    cpu_producer = Field()
    cpu = Field()
    gpu = Field()
    memory = Field()
    drive_type = Field()
    drive_capacity = Field()
    mb_chipset = Field()