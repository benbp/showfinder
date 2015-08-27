#!/usr/bin/python

import sys
import os
import re
import logging
import scrapy
from scrapy.crawler import CrawlerProcess

# I couldn't get any of the ways to disable/redirect logging to work that were
# detailed in the scrapy documentation :(
logging.disable(logging.DEBUG)
logging.disable(logging.INFO)

class TourSpider(scrapy.Spider):
    name = 'tour spider'
    # city, artist, start_urls overriden by subclass created by make_spider()
    city = None
    artist = None
    start_urls = []

    def parse(self, response):
        tour_words = ['tour', 'show', 'concert', 'event', 'schedule']
        tour_re = '|'.join(['.*' + s + '.*' for s in tour_words])
        for href in response.xpath('//a/@href').re(tour_re):
            tour_url = response.urljoin(href)
            yield scrapy.Request(tour_url, callback=self.parse_tour_data)

    def parse_tour_data(self, response):
        if re.search(self.city, response.body, re.IGNORECASE):
            print_match(self.artist, response.url, self.city)


def print_match(artist, url, city):
    print '{0} is coming to {1}! (see {2})'.format(artist, city, url)


def get_urls():
    with open('./urls.txt') as urls:
        lines = urls.read().splitlines()
    return [line.split(',') for line in lines]


def make_spider(artist, url, city):
    props = {'start_urls': [url], 'city': city, 'artist': artist}
    return type(artist + 'Spider', (TourSpider, ), props)


def run(urls, city):
    process = CrawlerProcess()
    spiders = [make_spider(artist, url, city) for artist, url in urls]
    for spider_cls in spiders:
        process.crawl(spider_cls)
    # the script will block here until the crawling is finished
    process.start()


def main():
    if not os.path.isfile('./urls.txt'):
        print 'Please create a urls.txt file. See README.md for instructions.'
        sys.exit(1)

    if len(sys.argv) != 2:
        print 'Expected a city to be specified: ./scrape.py <city>'
        sys.exit(2)
    else:
        city = sys.argv[1]

    artist_urls = get_urls()

    print 'Searching artists: '
    print artist_urls
    print '-'*80

    run(artist_urls, city)

    print '-'*80
    print 'DONE'

if __name__ == '__main__':
    main()
