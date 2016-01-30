import json

import scrapy
from scrapy.http.headers import Headers

RENDER_HTML_URL = "http://127.0.0.1:8050/render.html"

class MySpider(scrapy.Spider):
    start_urls = ["http://example.com", "http://example.com/foo"]

    def start_requests(self):
        for url in self.start_urls:
            body = json.dumps({"url": url, "wait": 0.5})
            headers = Headers({'Content-Type': 'application/json'})
            yield scrapy.Request(RENDER_HTML_URL, self.parse, method="POST",
                                 body=body, headers=headers)

    def parse(self, response):
        le = LinkExtractor()
        for link in le.extract_links(response):
            yield scrapy.Request(link.url, self.parse_link, meta={
                'splash': {
                    'args': {'har': 1, 'html': 0},
                }
            })

    def parse_link(self, response):
        res = json.loads(response.body)
        print(res["har"]["log"]["pages"])
