# -*- coding: utf-8 -*-
import scrapy


class CitacoesSpider(scrapy.Spider):
    name = 'citacoes'
    allowed_domains = ['www.imdb.com']
    start_urls = ['https://www.imdb.com/calendar/']

    def parse(self, response):
        for data in response.css('div#main h4'):
            yield {
                'data_de_lancamento': data.css('h4::text').get(),
            }
        for data in response.css('div#main ul'):
            yield{
                'titulo': data.css('li a::text').get()
            }
        
        proximoPais = response.css('div#sidebar div.aux-content-widget-3 ul li a::attr(href)').get()
        if proximoPais is not None:
            proximoPais = response.urlJoin(proximoPais)
            yield scrapy.Request(proximoPais, callback = self.parse)
