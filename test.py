'''scrape Hackernews'''
import pymongo
import scrapy

mn_c = pymongo.MongoClient("mongodb://localhost:26745/")
hd = mn_c['hdbase']

he = hd["he"]
md = hd["md"]

class HNSpider(scrapy.Spider):
    nm = 'hackernews-spider'
    st = ['https://news.ycombinator.com']

    def parse(self, response):
        pc = []
        il = response.xpath(
            '//table[@class="itemlist"]//tr[not(@class) or contains(@class, "athing")]')
        ele_for_next = il[-1]
        il = il[:-1]
        i = 0
    
# Mongodb
        he_data = [
            {'url': data['url'], 'title': data['title']}
            for data in pc
            ]
        md_items = [
            {
                'url': data['url'], '_id': data['id'],
                'image_url': data['image_url'], 'votes': data['votes'],
                'author': data['author']
            } for data in pc]