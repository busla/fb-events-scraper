from scrapy.item import Item, Field

class FbEventsItem(Item):
    event_id = Field()
    event_url = Field()
    event_title = Field()
    time = Field()
    date = Field()
    event_image = Field()
    venue = Field()
    venue_url = Field()
    event_location = Field()
    