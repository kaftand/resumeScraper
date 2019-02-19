import scrapy
from .. import items

class ResumeScraper(scrapy.Spider):
    name = "myResumeScraper"

    def start_requests(self):
        yield scrapy.Request(url = "http://dkaf.coffee/resumeLinks.html", callback=self.parseResumeLists)

    def parseResumeLists(self, response):
        links = response.css("ul#resumeStuff a::attr(href)").extract()
        for link in links:
            yield response.follow(url = link, callback = self.parse)

    def parse(self, response):
        if "head" in response.url.lower():
            tag = "head"
        else:
            tag = "body"
        thisItem = items.MyprojectItem()
        thisItem["text"] = response.text
        thisItem["tag"] = tag
        yield thisItem




