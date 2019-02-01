from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Join

class DailyCoffeeNewsLoader(ItemLoader):
    default_input_processor = MapCompose(lambda s: unicode(s, "utf-8"), unicode.strip)
    default_output_processor = Join()

    title_in = MapCompose(unicode.strip, unicode.title)
    title_out = Join()

    text_in = MapCompose(unicode.strip)
    text_out = Join()