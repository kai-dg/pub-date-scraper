#!/usr/bin/env python3
"""Entry point for pub-scraping"""
from sys import argv
from scrapers.base_parse import BaseParse
from scrapers.meta_scraper import MetaScraper


def find_pub():
    """Finds the publication date of the first argument

    Args:
        argv[1](str): url of the page you want to find the date in
    """
    page = BaseParse(argv[1])
    meta = MetaScraper(page.soup)
    print(meta.s_pub)
    print(meta.a_pub)

if __name__ == "__main__":
    find_pub()
