# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MeinvnetworkPipeline:
    fp = None

    # 重写父类的一个方法：该方法只在爬虫开始的时候被调用一次
    def open_spider(self, spider):
        print('开始爬虫。。。。')
        self.fp = open('./img_name.txt', 'w', encoding='utf-8')

    def close_spider(self, spider):
        print('爬虫结束!!!')
        self.fp.close()

    def process_item(self, item, spider):
        name = item['name']
        self.fp.write(name+'\n')
        return item

