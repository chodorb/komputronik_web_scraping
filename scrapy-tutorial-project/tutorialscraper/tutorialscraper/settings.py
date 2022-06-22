BOT_NAME = 'tutorialscraper'

SPIDER_MODULES = ['tutorialscraper.spiders']
NEWSPIDER_MODULE = 'tutorialscraper.spiders'

ROBOTSTXT_OBEY = False

FILE_NAME = 'output.csv'
FEED_EXPORT_FIELDS = ['name','producer','price','cpu_producer','cpu','gpu','memory','drive_type','drive_capacity','mb_chipset']
ITEM_PIPELINES = {
    'tutorialscraper.pipelines.SpecsExportPipeline':600,
}