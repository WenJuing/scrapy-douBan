# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import re


class RankPipeline:
    def process_item(self, item, spider):
        # 存储排行榜中的电影信息
        with open("douban_rank.txt", "a+", encoding="utf8") as file:
            title = re.sub('[ /]', '', item['title'][0])
            time = re.sub('[(].*', '', item['detail'][0])
            actor = re.sub('[\\d|-]*', '', item['detail'][0])
            file.write("\n片名：" + title.strip() + "\n")
            file.write("时间：" + time.strip() + "\n")
            file.write("演员：" + actor.strip() + "\n")
            file.write("评分：" + item['rank'][0] + "\n")
            file.write("评分人数：" + item['ranked_count'][0] + "\n")
        return item


class Top250Pipeline:
    def process_item(self, item, spider):
        # 存储top250中的电影信息
        with open("douban_top250.txt", "a+", encoding="utf8") as file:
            director_actor = re.split('主演', item['actor'][0])  # 把导演和演员分开
            director_actor[0] = re.sub(' ', '', director_actor[0])
            director_actor[1] = re.sub(' ', '', director_actor[1])
            item['actor'][1] = re.sub(' ', '', item['actor'][1])
            file.write("-------------------------------------[No. " + str(item['number']) + "]---")
            file.write("\n片名：" + item['title'][0])
            file.write(director_actor[0] + "\n")
            file.write("演员" + director_actor[1] + "\n")
            file.write("年份/国家/类型：" + item['actor'][1].strip() + "\n")
            file.write("评分：" + item['rank'][0] + "\n")
            file.write("评分人数：" + item['ranked_count'][0] + "\n")
        return item
