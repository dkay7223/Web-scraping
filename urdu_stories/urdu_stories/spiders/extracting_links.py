# filename: extracting_links.py
import scrapy


class extracting_links(scrapy.Spider):
    name = "extracting_links"
    start_urls = ["https://www.urduzone.net"]

    def parse(self, response):
        stories = response.css("h3.entry-title")
        for story in stories:
            yield {
                "name": story.css("a::text").get(),
                "link": story.css("a").attrib["href"],
            }
