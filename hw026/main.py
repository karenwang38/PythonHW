import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


def main():
    target_urls = [
        'https://www.ptt.cc/bbs/joke/M.1585109572.A.0D8.html',
        'https://www.ptt.cc/bbs/NBA/M.1585343654.A.A77.html'
    ]
    process = CrawlerProcess(get_project_settings())
    process.crawl('PTTFirst', start_urls=target_urls, filename='test.json')
    process.start()

if __name__ == '__main__':
    main()



