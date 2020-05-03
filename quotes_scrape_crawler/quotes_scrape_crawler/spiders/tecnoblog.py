# -*- coding: utf-8 -*-
import scrapy


class tecnoblogSpider(scrapy.Spider):
    name = 'tecnoblog'
    allowed_domains = ['tecnoblog.net']
    start_urls = ['https://tecnoblog.net/page/2/']

    def parse(self, response):
        for data in response.css('article.bloco'):
            yield {
                'titulo': data.css('h2 a::text').get(),
                'data': data.css('div.info time::text').get(),
                'autor': data.css('div.info a::text').get()
            }
        
        proximaPagina = response.css('a#mais::attr(href)').get()

        if proximaPagina is not None:
            proximaPagina = response.urlJoin(proximaPagina)
            yield scrapy.Request(proximaPagina, callback = self.parse)