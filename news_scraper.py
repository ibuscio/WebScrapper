# -*- coding: utf-8 -*-
import argparse
import logging
import datetime
import csv
from common import config

import news_page_objects as news

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)


def _news_scraper(news_site_uid):
    host = config()['news_sites'][news_site_uid]['url']
    logging.info('Beginning scraper for {}'.format(host))
    homepage = news.HomePage(host)
    links = homepage.article_links
    homepage.save_articles(news_site_uid, links)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    new_sites_choices = list(config()['news_sites'].keys())
    parser.add_argument('news_sites',
                        help='The news site that you want to scrape',
                        type=str,
                        choices=new_sites_choices)

    args = parser.parse_args()
    _news_scraper(args.news_sites)
