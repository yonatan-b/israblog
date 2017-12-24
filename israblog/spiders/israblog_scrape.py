# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from israblog.items import IsrablogItem
import re

class IsrablogScrapeSpider(CrawlSpider):
    name = 'israblog_scrape'
    allowed_domains = ['israblog.nana10.co.il']
    start_urls = ['http://israblog.nana10.co.il']

    rules = (
        Rule(LinkExtractor(allow='.*?israblog\.nana10\.co\.il\/blogread\.asp\?blog=\d+$'), callback=None, follow=True),
        Rule(LinkExtractor(allow='.*?blogread\.asp\?blog=\d.*?year=\d+.*?month=\d+.*?day=\d.*?pagenum=\d*.*'), callback=None, follow=True),
        Rule(LinkExtractor(allow='.*?blogread\.asp\?blog=\d+.*?blogcode=\d+$'), callback='parse_item', follow=True),

    )

    def parse_item(self, response):
        selector=scrapy.selector.Selector(response=response)

        nickname = ''
        content= selector.xpath('//head/meta[@name="keywords"]/@content').extract_first()
        if (content):
            content_list = re.split(',',content.strip())
            if len(content_list) >= 4: 
                nickname = content_list[-4]

        
        post_title=''
        post_title = selector.xpath('//head/meta[@property="og:title"]/@content').extract_first()

        post_url=response.url

        post_content = ''
        post_content_list = selector.xpath('.//span[@class="postedit"]/descendant::*/text()').extract()
        if post_content_list:
            post_content =' '.join(post_content_list).replace('\xa0',' ').strip() # \xa0 is &nbsp; (non-breaking space) character

        
        post_date,post_hour = ['','']
        xpath_str = r'//div[contains(.,' + '"' +nickname + '"'  + r')][@dir="rtl"]/text()'
        post_footer = selector.xpath(xpath_str).extract()
        if post_footer:
            post_footer = ''.join(post_footer).strip()
            post_date,post_hour = re.findall('.*?(\d+\/\d+/\d{3,4}).*?(\d{2,2}:\d{2,2}).*',post_footer)[0]

        personal_details = selector.xpath('//td[@id="ParentColumn_2" or @id= "ParentColumn_1" ]/div[contains(.,"כינוי")]').extract_first()
        gender=''
        age=''
        BAT = re.findall("בת:.*?(\d{2,2})",personal_details)
        BEN = re.findall("בן:.*?(\d{2,2})",personal_details)
        GIL = re.findall("גיל:.*?(\d{2,2})",personal_details)
        MINN = re.findall("מין:.*?(\w{3,4})",personal_details)
        if (BAT):
            gender="בת"
            age=BAT[0]
        if (BEN):
            gender="בן"
            age=BEN[0]
        if (GIL):
            age=GIL[0]
        if (MINN):
            gender= MINN[0]


        item = IsrablogItem()
        item['nickname']  = nickname
        item['blogger_age']= age
        item['blogger_gender'] = gender
        item['post_title']= post_title
        item['post_content']=post_content
        item['post_date']=post_date
        item['post_hour']=post_hour
        item['post_url']=post_url
        
        return item
 




        # item = {}
        # #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        # #i['name'] = response.xpath('//div[@id="name"]').extract()
        # #i['description'] = response.xpath('//div[@id="description"]').extract()
        # return i
