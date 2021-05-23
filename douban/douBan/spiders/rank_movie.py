import scrapy
from ..items import DoubanItem


class RankMovieSpider(scrapy.Spider):
    name = 'rank_movie'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/chart']

    def parse(self, response):
        items = []
        subselector = response.xpath('//div[@class="pl2"]')

        for get_info in subselector:
            item = DoubanItem()
            item['title'] = get_info.xpath('./a/text()').extract()
            item['detail'] = get_info.xpath('./p/text()').extract()
            item['rank'] = get_info.xpath('./div/span[@class="rating_nums"]/text()').extract()
            item['ranked_count'] = get_info.xpath('./div/span[@class="pl"]/text()').extract()
            items.append(item)

        return items
