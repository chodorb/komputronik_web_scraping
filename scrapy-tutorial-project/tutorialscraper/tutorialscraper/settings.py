BOT_NAME = 'tutorialscraper'

SPIDER_MODULES = ['tutorialscraper.spiders']
NEWSPIDER_MODULE = 'tutorialscraper.spiders'

ROBOTSTXT_OBEY = True

FILE_NAME = 'output.csv'
FEED_EXPORT_FIELDS = ['name','produceer','price','cpu_producer','cpu','gpu','memory','drive_type','drive_capacity','mb_chipset']
ITEM_PIPELINES = {
    'tutorialscraper.pipelines.SpecsExportPipeline':600,
}