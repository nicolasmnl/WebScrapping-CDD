import scrapy
from .utils import get_links_deputados


class QuotesSpider(scrapy.Spider):
    name = "miles_morales"

    def start_requests(self):
        
        urls = get_links_deputados()
        print(urls)
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        filename = f'https://www.camara.leg.br/deputados/'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')
