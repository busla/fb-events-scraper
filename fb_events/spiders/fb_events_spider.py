from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from fb_events.items import FbEventsItem
import datetime


class FbEventsSpider(BaseSpider):
    name = "fb_events"
    allowed_domains = ["http://facebook.com"]
    start_urls = [
        "https://www.facebook.com/rvksoundsystem/events"
    ]

    def prepare_comment(self, html):
        cleaned = (html.replace('<!-- ','').replace(' -->',''))
        return cleaned

    def extract_id(self, event_url):
        event_url = [i.split('/')[2] for i in event_url]
        return event_url
            
    def parse(self, response):
    	fb_html = Selector(response)
    	html_comment = fb_html.xpath('//code[4]').extract()
    	html_clean = [self.prepare_comment(s) for s in html_comment]
        html_joined = ''.join(html_clean)

        fb_selector = Selector(response=None, text=html_joined, type="html")

    	events = fb_selector.xpath('//table["@class=eventsGrid"]/tbody')
    	items = []
        for event in events:
            item = FbEventsItem()
            item['event_id'] = self.extract_id(event.xpath('tr/td["@class=eventsFirstCol"]/table/tbody/tr/td[2]/div[1]/a/@href').extract())
            item['event_url'] = event.xpath('tr/td["@class=eventsFirstCol"]/table/tbody/tr/td[2]/div[1]/a/@href').extract()
            item['event_title'] = event.xpath('tr/td["@class=eventsFirstCol"]/table/tbody/tr/td[2]/div[1]/a/text()').extract()
            item['time'] = event.xpath('tr/td["@class=eventsFirstCol"]/table/tbody/tr/td[2]/div[2]/span[2]/text()').extract()
            item['date'] = event.xpath('tr/td["@class=eventsFirstCol"]/table/tbody/tr/td[2]/div[2]/span[1]/text()').extract()
            item['event_image'] = event.xpath('tr/td["@class=eventsFirstCol"]/table/tbody/tr/td[1]/a/img/@src').extract()
            item['venue'] = event.xpath('tr/td["@class=eventsSecondCol"]/div["@class=eventLocation"]/div/a/text()').extract()
            item['venue_url'] = event.xpath('tr/td["@class=eventsSecondCol"]/div["@class=eventLocation"]/div/a/@href').extract()
            item['event_location'] = event.xpath('tr/td["@class=eventsSecondCol"]/div["@class=eventLocation"]/a/strong/text()').extract()
            items.append(item)
        return items