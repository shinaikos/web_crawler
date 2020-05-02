# -*- coding: utf-8 -*-
import scrapy


class CitacoesSpider(scrapy.Spider):
    name = 'citacoes'
    allowed_domains = ['www.imdb.com']
    start_urls = ['https://www.imdb.com/calendar/']

    def parse(self, response):
        for data in response.css('div#main'):
            yield {
                'data_de_lancamento': data.css('h4::text').getall(),
                'titulo': data.css('a::text').getall()
            }
