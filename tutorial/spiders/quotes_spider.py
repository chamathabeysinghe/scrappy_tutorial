import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        with open('urls.csv') as f:
            urls = f.readlines()
        urls = [x.strip() for x in urls]

        # urls = [
        #     'http://www.observereducation.lk/2017/08/01/enter-the-final-year-bba-awarded-by-ipac-school-of-business-france/',
        #     "http://www.observereducation.lk/2016/11/01/anc-postgraduate-school-opens-applications-for-jan-2017-intake-revamping-cima-mba-for-global-competitiveness/"
        # ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print(response.url)
        title = response.css('h1.entry-title::text').extract_first()
        content = response.css('div.entry-content')[0].css('p').extract_first()
        author = response.xpath('//div[@class="entry-meta clearfix"]/span[@class="post-author"]/span/a/text()').extract_first()
        category = response.xpath('//div[@class="entry-meta clearfix"]/span[@class="cat-links"]/a/text()').extract_first()
        yield {
            'title': title,
            'content': content,
            'author': author,
            'category': category
        }
        # for quote in response.css('div.quote'):
        #     yield {
        #         'text': quote.css('h1.text::text').extract_first(),
        #         'author': quote.css('small.author::text').extract_first(),
        #         'tags': quote.css('div.tags a.tag::text').extract(),
        #     }
        # for a in response.css('li.next a'):
        #     yield response.follow(a, callback=self.parse)

