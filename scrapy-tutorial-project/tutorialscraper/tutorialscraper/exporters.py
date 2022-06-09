from scrapy.exporters import CsvItemExporter

class SpecsItemExporter(CsvItemExporter):
    
    def __init__(self, file, **kwargs):
        super().__init__(file)