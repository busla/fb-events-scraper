# Scrapy settings for fb_events project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'fb_events'

SPIDER_MODULES = ['fb_events.spiders']
NEWSPIDER_MODULE = 'fb_events.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'fb_events (+http://www.yourdomain.com)'
