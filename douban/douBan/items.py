# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()          # 电影名
    actor = scrapy.Field()          # 演员（导演）
    detail = scrapy.Field()         # 电影细节
    rank = scrapy.Field()           # 评分
    ranked_count = scrapy.Field()   # 评分人数
    number = scrapy.Field()         # No.号
