# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JusticescraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class NewsItem(scrapy.Item):
    title = scrapy.Field()
    date = scrapy.Field()
    subtitle =  scrapy.Field()
    fulltext =  scrapy.Field()
    url = scrapy.Field()
    topic_category = scrapy.Field()
    node_component = scrapy.Field()
    office  = scrapy.Field()
