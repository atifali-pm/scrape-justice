import scrapy

from justicescraper.items import NewsItem

class JusticespiderSpider(scrapy.Spider):
    name = "justicespider"
    allowed_domains = ["www.justice.gov"]
    start_urls = ["https://www.justice.gov/news"]

    def parse(self, response):
        justice_news = response.css('div.rows-wrapper div.views-row a')

        for link in justice_news:
            news_url = link.css('a').attrib['href']
            news_url = 'https://www.justice.gov' + news_url
           

            yield response.follow(news_url, callback=self.parse_news_page)

    
        links = response.css("ul.usa-pagination__list li a")
        for link in links:
            if "Next page" in link.get():
                print("********************************")
                print(link.attrib['href'])
                print("********************************")
                next_page_url = 'https://www.justice.gov/news' + link.attrib['href']
                yield response.follow(next_page_url, callback=self.parse)

    
    def parse_news_page(self, response):

        news_item = NewsItem()
        details = response.css('div.node-body .field_body p')

        paragraph = ""
        for detail in details:
            paragraph += detail.css('::text').get()

        
        news_item['title'] = response.css('h1.page-title span ::text').get()
        news_item['date'] = response.css('div.node-updated-date ::text').get()
        news_item['subtitle'] = response.css('div.node-subtitle .field_subtitle ::text').get()
        news_item['fulltext'] = paragraph
        news_item['url'] = response.request.url
        news_item['topic_category'] = response.css('div.node-topics .field__item ::text').get()
        news_item['node_component'] = response.css('div.node-component .field__item a ::text').get()
        news_item['office'] = response.css('div.node-info-box div.node-office ::text').get()

        yield news_item
    
        



        
