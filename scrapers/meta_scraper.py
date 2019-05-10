#!/usr/bin/env python3
"""meta_scraper"""
from bs4 import BeautifulSoup

class MetaScraper:
    """MetaScraper

    Args:
        soup (obj): BeautifulSoup obj containing parsed link
    """
    def __init__(self, soup):
        self.soup = soup
        self.s_pub = self.get_shareaholic()
        self.a_pub = self.get_article()

    def get_shareaholic(self):
        for tag in self.soup.find_all("meta"):
            if tag.get("name", None) == "shareaholic:article_published_time":
                return tag.get("content")

    def get_article(self):
        for tag in self.soup.find_all("meta"):
            if tag.get("property", None) == "article:published_time":
                return tag.get("content")
