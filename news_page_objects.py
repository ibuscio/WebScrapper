import requests
import datetime
import csv
from bs4 import BeautifulSoup

from common import config


class HomePage:

    def __init__(self, host):
        self._html = None
        self._links = None
        self._visit(host)

    @property
    def article_links(self):

        sections = self._html.findAll('div', attrs={'class': 'headline normal normal-style'})
        link_sections = [section.a.get('href') for section in sections]
        return link_sections

    def save_articles(self, news_site_uid, links):
        now = datetime.datetime.now().strftime('%Y-%m-%d')
        out_file_name = '{news_site_uid}_{datetime}_articles.csv'.format(news_site_uid=news_site_uid, datetime=now)
        with open(out_file_name, mode='+w') as f:
            writer = csv.writer(f)
            writer.writerow(links)

    def _visit(self, host):
        response = requests.get(host)
        response.raise_for_status()

        self._html = BeautifulSoup(response.text, 'html.parser')










