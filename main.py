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
    page = BaseParse(argv[1])
    if page.soup is None:
        return "[ERROR] Could not get request of the URL."

    wayback = Wayback(argv[1])
    meta = MetaScraper(page.soup)
    meta_list = [meta.s_pub, meta.a_pub, meta.t_pub]

    if wayback.wayback_time:
        print("\n======== Wayback =======")
        print(wayback.wayback_time)
        print("========================\n")
    else:
        print("\n========= Meta =========")
        nd_counter = 0
        for i in meta_list:
            if i is not None:
                nd_counter += 1
                print(i)
        if nd_counter == 0:
            print("Metadata: n.d. (No Date)")
        print("========================\n")

if __name__ == "__main__":
    find_pub()
