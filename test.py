
from korea_news_crawler.articlecrawler import ArticleCrawler

keyword = input('키워드를 입력하시오: ')
Crawler = ArticleCrawler()
Crawler.set_category('정치')
Crawler.set_date_range('2024-03-01', '2024-03-31')
Crawler.start(keyword)