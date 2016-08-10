# -*- coding: utf-8 -*-

import scrapy
import scrapy.loader
import scrapy.loader.processors as scrapy_processors
import dateutil.parser

class VoterListItem(scrapy.Item):
    state  = scrapy.Field()
    county = scrapy.Field()
    date   = scrapy.Field(
        input_processor=scrapy_processors.MapCompose(dateutil.parser.parse),
        output_processor=scrapy_processors.Compose(
            scrapy_processors.TakeFirst(),
            lambda date: date.strftime('%Y%m%d')
        )
    )
    list_format = scrapy.Field()
    file_url    = scrapy.Field()
    file_data   = scrapy.Field()


    def file_name(self):
        return '-'.join((
            self.get('state'),
            self.get('county'),
            self.get('date'),
            self.get('list_format'),
        )) + '.csv'


class VoterListLoader(scrapy.loader.ItemLoader):
    default_item_class       = VoterListItem
    default_output_processor = scrapy_processors.TakeFirst()
