import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


def main():
    target_board = ['Gossiping']
#     target_board = ['Stock', 'Gossiping', 'Lifeismoney', 'movie', 'cookclub', 'Finance']
    process = CrawlerProcess(get_project_settings())

    for board in target_board:
        print('MAIN():', board)
        process.crawl('PTTCrawler',  board=board)
#     process.crawl('PTTCrawler',  board=target_board)
    process.start()



if __name__ == '__main__':
    main()
