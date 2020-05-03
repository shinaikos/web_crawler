# -*- coding: utf-8 -*-
import scrapy


class udemySpider(scrapy.Spider):
    name = 'udemy'
    allowed_domains = ['https://www.udemy.com/']
    start_urls = ['https://www.udemy.com/topic/javascript/']

    def parse(self, response):
        for data in response.css('div.list-view-course-card--content--1TGG4'):
            yield {
                'titulo': data.css('a h4::text').get()
            }