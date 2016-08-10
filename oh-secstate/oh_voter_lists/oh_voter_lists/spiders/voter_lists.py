# -*- coding: utf-8 -*-

import scrapy

from oh_voter_lists.items import VoterListItem, VoterListLoader


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
            voter_list_loader = VoterListLoader(selector=row)

            voter_list_loader.add_xpath('county',      '(.//td)[1]//text()')
            voter_list_loader.add_xpath('date',        '(.//td)[2]/text()')
            voter_list_loader.add_xpath('file_url',    './/a[contains(., "Download")]/@href')
            voter_list_loader.add_value('state',       'OH')
            voter_list_loader.add_value('list_format', 'SECSTATE')

            voter_list_item = voter_list_loader.load_item()
            print('  Found list for county:               %s' % voter_list_item['county'])

            yield voter_list_item

    def closed(self, reason):
        if reason == 'finished':
            print('\nScraping complete.')
        else:
            print('\nScraping ended: %s' % reason)
