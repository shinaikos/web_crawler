# -*- coding: utf-8 -*-
import scrapy


class testeSpider(scrapy.Spider):
    name = 'teste'
    allowed_domains = ['https://www.techtudo.com.br']
    start_urls = ['https://www.techtudo.com.br/noticias/plantao/feed/pagina-2.html']

    def parse(self, response):
        for data in response.css('div.feed-post-body'):
            yield {
                'titulo': data.css('a.feed-post-link::text').get(),
                'resumo': data.css('div.feed-post-body-resumo::text').get(),
                'tempo': data.css('span.feed-post-datetime::text').get(),
                'secao': data.css('span.feed-post-metadata-section::text').get()
            }
        proximaPagina = response.css('div.load-more a::attr(href)').get()
        if proximaPagina is not None:
            proximaPagina = response.urlJoin(proximaPagina)
            yield scrapy.Request(proximaPagina, callback = self.parse)
