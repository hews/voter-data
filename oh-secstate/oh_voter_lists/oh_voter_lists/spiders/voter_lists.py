# -*- coding: utf-8 -*-
import scrapy

from oh_voter_lists.items import VoterListItem, VoterListLoader

class ExampleSpider(scrapy.Spider):
    name = "example"
    allowed_domains = ["example.com"]
    start_urls = (
        'http://www.example.com/',
    )

    def parse(self, response):
        pass

class VoterListsSpider(scrapy.Spider):
    LOG_ENABLED = False

    name = 'voter_lists'
    start_urls = ['http://www6.sos.state.oh.us/ords/f?p=111:1']

    print('\nLoaded spider %s. Beginning to scrape…\n' % name)


    def parse(self, response):
        print('Parsing page at %s:' % response.url)

        row_xp = '//a[contains(., "Download")]/ancestor::tr[1]'
        rows   = response.selector.xpath(row_xp)
        length = len(rows)

        for index, row in enumerate(rows):
            if index == 0:
                voter_list_loader = VoterListLoader(selector=row)
                voter_list_loader.add_xpath('county',    '(.//td)[1]//text()')
                voter_list_loader.add_xpath('date',      '(.//td)[2]/text()')
                voter_list_loader.add_xpath('file_urls', './/a[contains(., "Download")]/@href')

                voter_item = voter_list_loader.load_item()

                # self.download_list_file(index+1, length, voter_list)

                print(voter_item)
                yield voter_item


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
