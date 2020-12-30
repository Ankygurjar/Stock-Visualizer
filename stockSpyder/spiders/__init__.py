# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import scrapy

class StockSpyder(scrapy.Spider):

    name = "StockSpyder"

    def start_requests(self):

        url = "https://ca.finance.yahoo.com/quote/AMZN/history?p=AMZN"

        yield scrapy.Request(url = url, callback = self.parse)

    def parse(self, response):

        page = response.url.split("/")[-2]

        filename = f'./crawledData/stock-{page}.html'

        with open(filename, 'wb') as f:
            f.write(response.body)
