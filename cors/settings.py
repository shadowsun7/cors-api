# Scrapy settings for cors project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'cors'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['cors.spiders']
NEWSPIDER_MODULE = 'cors.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

ITEM_PIPELINES = [
	'cors.pipelines.CorsPipeline',
]

