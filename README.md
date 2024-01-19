**Assignment: Web Scraping with Scrapy - Collecting Urdu Stories**

### **1. Objective**
The objective of this assignment is to develop a Scrapy spider to scrape the website (https://www.urduzone.net) and extract Urdu stories while removing tags and non-Urdu words.

### **2. Instructions**

#### **2.1 Setup**
1. Create a new Scrapy project for this assignment using the command: `scrapy startproject urdu_stories`.

#### **2.2 Spider Development**
1. Inside your Scrapy project, create a new spider named ‘I20XXXXurdu_stories_spider’ to scrape (https://www.urduzone.net), where I201234 is your roll number.
2. Set the start URL to (https://www.urduzone.net).
3. Configure the spider to crawl through the website and extract the necessary data.
4. Use Scrapy selectors to extract text content from the website.

#### **2.3 Data Extraction**
1. Extract the text of the stories from the website while removing any HTML tags.
2. Implement a mechanism to filter out non-Urdu words and numbers, keeping only the Urdu text.

#### **2.4 Data Storage**
1. Store the collected Urdu stories in a structured format such as a CSV file within the Scrapy project directory.

#### **2.5 Documentation**
1. Provide clear and concise documentation explaining your approach and any challenges faced, written in LaTeX.
2. Include comments in your spider’s code to explain the logic and any important steps.

---

**Note:**
- Ensure that your spider adheres to ethical scraping practices.
- Test your spider on a small scale before running it extensively.
- Follow the Scrapy documentation for guidance: [Scrapy Documentation](https://docs.scrapy.org/en/latest/)

*Happy Coding!*
