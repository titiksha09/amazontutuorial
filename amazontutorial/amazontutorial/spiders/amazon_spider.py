import scrapy
from ..items import AmazontutorialItem


class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'
    #allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.in/s?k=books']

    def parse(self, response):
        items = AmazontutorialItem()
        product_name = response.css(" .a-size-medium::text").get()
        product_author = response.css(".a-color-secondary .a-size-base+ .a-size-base").css('::text').get()
        product_price = response.css(".s-price-instructions-style .a-price-whole").css('::text').get()
        product_imagelink = response.css(".s-image::attr(src)").get()

        items['product_name'] = product_name
        items['product_author'] = product_author
        items['product_price'] = product_price
        items['product_imagelink'] = product_imagelink

        yield items



