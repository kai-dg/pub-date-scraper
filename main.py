#!/usr/bin/env python3
"""Entry point for pub-scraping"""
from sys import argv
from scrapers.base_parse import BaseParse
from scrapers.meta_scraper import MetaScraper
from wayback import Wayback


def find_pub():
    """Finds the publication date of the first argument

    Args:
        argv[1](str): url of the page you want to find the date in
    """
    nd_counter = 0
    page = BaseParse(argv[1])
    if page.soup is None:
        return "[ERROR] Could not get request of the URL."

    meta = MetaScraper(page.soup)
    meta_list = [meta.s_pub, meta.a_pub, meta.t_pub]
    for i in meta_list:
        if i is not None:
            nd_counter += 1
            print(i)

    wayback = Wayback(argv[1])
    print(wayback.wayback_time)

    if nd_counter == 0:
        print("Metadata: n.d. (No Date)")


if __name__ == "__main__":
    find_pub()
