import scrapy


from scrapy_selenium import SeleniumRequest


class VbplSpider(scrapy.Spider):
    name = "vbpl"

    def start_requests(self):
        yield SeleniumRequest(url="https://vbpl.vn/Pages/portal.aspx", callback=self.parse)

    def parse(self, response):
        for link in response.css("a::attr(href)").getall():
            if link.endswith(".pdf"):
                yield {"file_url": response.urljoin(link)}
def parse(self, response):
    print(response.text[:1000])  # In thử 1000 ký tự đầu của HTML
