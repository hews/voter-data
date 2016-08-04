import scrapy
import scrapy.loader
import dateutil.parser as datep

from scrapy.loader.processors import TakeFirst

# TODO (PJ): fail if page doesn't load

class VoterList(scrapy.Item):
    state       = scrapy.Field(default='OH')
    county      = scrapy.Field()
    date        = scrapy.Field() # TODO (PJ): add a serializer to store this as datetime
    list_format = scrapy.Field(default='SECSTATE')
    url         = scrapy.Field()

    def file_name(self):
        return '-'.join((
            self.get('state'),
            self.get('county'),
            self.get('date'),
            self.get('list_format'),
        )) + '.csv'


class VoterListLoader(scrapy.loader.ItemLoader):
    default_item_class       = VoterList
    default_output_processor = TakeFirst()


class VoterListSpider(scrapy.Spider):
    LOG_ENABLED = False

    name = 'oh_voter_list_scraper'
    start_urls = ['http://www6.sos.state.oh.us/ords/f?p=111:1']

    print('Loaded %s. Beginning to scrape…\n' % name)


    def parse(self, response):
        print('Parsing page at %s:' % response.url)

        row_xp = '//a[contains(., "Download")]/ancestor::tr[1]'
        rows   = response.selector.xpath(row_xp)
        length = len(rows)

        for index, row in enumerate(rows):
            voter_list_loader = VoterListLoader(selector=row)
            voter_list_loader.add_xpath('county', '(.//td)[1]//text()')
            voter_list_loader.add_xpath('county', '(.//td)[2]/text()')
            voter_list_loader.add_xpath('url',    './/a[contains(., "Download")]/@href')

            # voter_list = VoterList(
            #     state='OH',
            #     county=county,
            #     date=datep.parse(date).strftime('%Y%m%d'),
            #     list_format='SECSTATE',
            #     url=url
            # )

            print(voter_list_loader.load_item())
            # self.download_list_file(index+1, length, voter_list)


    def download_list_file(self, index, length, voter_list):

        print(voter_list)
        # print('    Downloading entry (%i of %i) for %s at %s…' % (index, length, county, url))
        # yield scrapy.Request(url, self.download_and_unzip)


    # def parse_titles(self, response):
    #     for post_title in response.css('div.entries > ul > li a::text').extract():
    #         yield {'title': post_title}


    def closed(self, reason):
        if reason == 'finished':
            print('\nScraping complete.')
        else:
            print('\nScraping ended: %s' % reason)
