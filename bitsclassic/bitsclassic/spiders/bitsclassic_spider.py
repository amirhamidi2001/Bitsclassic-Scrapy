import json
import re

import scrapy
import requests

from bitsclassic.items import BitsclassicItem
from . import plugins


class BitsclassicSpider(scrapy.Spider):
    """
    Spider to crawl product data from bitsclassic.com.
    """

    name = "bitsclassic"
    start_urls = ["https://bitsclassic.com/fa"]

    def parse(self, response):
        """
        Parse the home page, extract category URLs, and start category crawling.
        """
        category_urls = response.css("ul.children a::attr(href)").getall()[1:]
        for category_url in category_urls:
            yield scrapy.Request(category_url, callback=self.parse_category)

    def parse_category(self, response):
        """
        Parse a category page, send a POST request to get the product list,
        and extract product URLs.
        """
        api_url = "https://bitsclassic.com/fa/Product/ProductList"
        category_id = re.search(r"/(\d+)-", response.url).group(1)
        num_products = 100

        data = {"Cats": str(category_id), "Size": str(num_products)}
        api_response = requests.post(api_url, data=data)
        response_dict = json.loads(api_response.text)
        html = response_dict.get("Html", "")

        # Extract product URLs from the returned HTML
        product_urls = re.findall(r'href="([^"]+)" class="imageWrap"', html)
        for product_url in product_urls:
            yield scrapy.Request(product_url, callback=self.parse_product)

    def parse_product(self, response):
        """
        Parse a product page and extract the desired fields into an item.
        """
        title = response.css('p[itemrolep="name"]::text').get()
        url = response.url
        categories = response.xpath('//div[@class="con-main"]//a/text()').getall()
        price = response.xpath(
            '//div[@id="priceBox"]//span[@data-role="price"]/text()'
        ).get()

        # Determine if the product exists (price present)
        if price is not None:
            price = price.strip()
            product_exist = True
        else:
            price = None
            product_exist = False

        # Generate a random ID (may be used later)
        plugins.gen_random_id()

        # Build the item
        item = BitsclassicItem()
        item["title"] = title.strip() if title else None
        item["categories"] = [cat.strip() for cat in categories][3:6]
        item["product_exist"] = product_exist
        # item["price"] = price   # commented because field is not defined in items.py
        item["url"] = response.url
        item["domain"] = "bitsclassic.com"
        item["currency"] = "تومان"

        yield item
