# -*- coding: utf-8 -*-

import os

BOT_NAME = 'oh_voter_lists'

SPIDER_MODULES   = ['oh_voter_lists.spiders']
NEWSPIDER_MODULE = 'oh_voter_lists.spiders'

# "Character: it's your responsibility"
USER_AGENT     = 'oh_voter_lists scraper found at: (+http://github.com/hews/voter-data)'
CONCURRENT_REQUESTS = 2

# FIXME (PJ): this is set to keep Scrapy from requesting another
#   robots.txt from the FTP server… Not because it fails to find
#   one, but because it check the URI's scheme and send the
#   correct headers/metadata in the request,
#   ```
#   Request(uri, meta={'ftp_user': 'anonymous', 'password': ''})
#   ```
#
#   Check: https://github.com/scrapy/scrapy/blob/master/scrapy/downloadermiddlewares/robotstxt.py
#
# ROBOTSTXT_OBEY = True

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
DOWNLOAD_DELAY = 3
CONCURRENT_REQUESTS_PER_DOMAIN = 2

# File pipeline setup…
CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
DATA_DIR    = os.path.abspath(os.path.join(CURRENT_DIR, '../../..', 'data'))
print('(File pipeline download target set to:)\n  %s' % DATA_DIR)

ITEM_PIPELINES = {
   # Instead of the using the default: scrapy.pipelines.files.FilesPipeline,
   #   must subclass it to send the necessary FTP headers/metadata
   'oh_voter_lists.pipelines.VoterListPipeline': 1
}
FILES_STORE        = DATA_DIR


# XXX NOTE (PJ): leftovers from scaffolding, but since I can't find them
#   as clearly in the docs, they are left for now.
#

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'oh_voter_lists.middlewares.MyCustomSpiderMiddleware': 543,
#}
# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'oh_voter_lists.middlewares.MyCustomDownloaderMiddleware': 543,
#}
# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}
# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
