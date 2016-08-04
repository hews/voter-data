import scrapy

import dateutil.parser as date

# TODO (PJ): fail if page doesn't load

class VoterListSpider(scrapy.Spider):
    LOG_ENABLED = False

    name = 'oh_voter_list_scraper'
    start_urls = ['http://www6.sos.state.oh.us/ords/f?p=111:1']

    print('Loaded %s. Beginning to scrape…\n' % name)

    def parse(self, response):
        print('Parsing page at %s:' % response.url)

        row_xps    = '//a[contains(., "Download")]/ancestor::tr[1]'
        county_xps = '(.//td)[1]//text()'
        date_xps   = '(.//td)[2]/text()'
        url_xps    = './/a[contains(., "Download")]/@href'

        for row in response.selector.xpath(row_xps):
            county = row.xpath(county_xps).extract()[0]
            date_  = row.xpath(date_xps).extract()[0]
            url    = row.xpath(url_xps).extract()[0]

            self.download_list_file(county, date_, url)
            # yield scrapy.Request(response.urljoin(url), self.parse_titles)

    def download_list_file(self, county, date_, url):
        file_name = 'OH-' + county + '.csv'

        print('    Found entry %s, (%s): %s' % (county, date_, url))
        print('    Name: %s\n' % file_name)

    # def parse_titles(self, response):
    #     for post_title in response.css('div.entries > ul > li a::text').extract():
    #         yield {'title': post_title}

    def closed(self, reason):
        if reason == 'finished':
            print('\nScraping complete.')
        else:
            print('\nScraping ended: %s' % reason)
