import scrapy
from scrapy.crawler import CrawlerProcess

from spiders.state_district_spider import stateSpider
from spiders.state_district_spider import districtSpider

def startCrawlers():
	process = CrawlerProcess({
	    'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.76 Safari/537.36'
	})
	process.crawl(stateSpider)
	process.crawl(districtSpider)
	process.start()


if __name__ == "__main__":
	startCrawlers()