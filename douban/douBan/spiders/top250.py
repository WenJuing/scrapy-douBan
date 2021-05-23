import scrapy
from scrapy.http.request import Request
from ..items import DoubanItem


class Top250Spider(scrapy.Spider):
    '''爬取豆瓣top250的电影信息'''
    name = 'top250'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/']
    i = 1   # 添加序号

    def start_requests(self):
        for offset in range(0, 226, 25):    # 每页25部电影，一共10页
            url = 'https://movie.douban.com/top250?start=' + str(offset) + '&filter='
            yield Request(url, callback=self.parse)

    def parse(self, response):
        item_250 = []
        subselector = response.xpath('//div[@class="info"]')

        for get_info in subselector:
            item = DoubanItem()
            item['number'] = self.i  # 给电影添加序号
            # 获取电影名、演员、评分和评分人数
            item['title'] = get_info.xpath('./div/a/span/text()').extract()
            item['actor'] = get_info.xpath('./div[@class="bd"]/p/text()').extract()
            item['rank'] = get_info.xpath('./div[@class="bd"]/div/span[@class="rating_num"]/text()').extract()
            item['ranked_count'] = get_info.xpath('./div[@class="bd"]/div/span[4]/text()').extract()
            item_250.append(item)
            self.i += 1
        return item_250
