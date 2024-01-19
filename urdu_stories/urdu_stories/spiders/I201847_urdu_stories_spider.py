# filename: I201847_urdu_stories_spider.py
import scrapy

#WE CAN REMOVE ANY OTHER YIELD TAGS, AND THAT WON'T Output any links and story names
# I have outputted the story names as well as their links for better manuevering.


class I201847UrduStoriesSpider(scrapy.Spider):
    name = "i201847_urdu_stories_spider"
    start_urls = ["https://www.urduzone.net"]

    def parse(self, response):
        # Extract story links from the main page
        stories = response.css('h3.entry-title')
        for story in stories:
            # Extract the link to the story
            link = story.css('a::attr(href)').get()
            
            # Create a new Scrapy request to follow the story link and invoke the parse_story callback
            yield scrapy.Request(link, callback=self.parse_story)

    def parse_story(self, response):
        # Extract the text inside the <p> element within the div with class "tdb-block-inner"
        paragraph_text = response.css('div.tdb-block-inner p::text').get()
        
        # Clean and yield the extracted data
        yield {
            'story_title': response.css('h1.entry-title::text').get(),  # Extract the story title
            'paragraph_text': paragraph_text.strip() if paragraph_text else None,  # Extracted paragraph text
            # Add more data extraction logic as needed
        }
