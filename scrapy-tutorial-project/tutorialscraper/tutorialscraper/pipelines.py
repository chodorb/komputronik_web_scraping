from itemadapter import ItemAdapter
from .settings import FEED_EXPORT_FIELDS
from tutorialscraper.exporters import SpecsItemExporter

class TutorialscraperPipeline:
    def process_item(self, item, spider):
        return item

class SpecsExportPipeline(object):
    def __init__(self,filename):
        self.filename = filename
        self.file_handle = None
        
    @classmethod
    def from_crawler(cls,crawler):
        output_file_name = crawler.settings.get('FILE_NAME')
        return cls(output_file_name)
    
    def open_spider(self,spider):
        file = open(self.filename,'wb')
        self.file_handle = file
        
        self.exporter = SpecsItemExporter(file)
        self.exporter.fields_to_export = FEED_EXPORT_FIELDS
        self.exporter.start_exporting()
        
    def close_spider(self):
        self.exporter.finish_exporting()
        
    def process_item(self, item ,spider):
        self.exporter.export_item(item)
        return item