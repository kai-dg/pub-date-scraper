#!/usr/bin/env python3
"""Entry point for pub-scraping"""
from datetime import date
from datetime import datetime
import re
from scrapers.base_parse import BaseParse
from scrapers.meta_scraper import MetaScraper
from sys import argv
from wayback import Wayback


def find_date(res):
    """Finds date difference from result to now

    Args:
        res(str): result from find_pub()
    """
    if res:
        curr = datetime.now().strftime("%Y-%m-%d").split("-")
        res_d = re.search(r"(\d+-\d+-\d+)", str(res)).group(1).split("-")

        d0 = date(int(curr[0]), int(curr[1]), int(curr[2]))
        d1 = date(int(res_d[0]), int(res_d[1]), int(res_d[2]))

        delta = d0 - d1

        return "This site is {} days old.\n".format(str(delta.days))
    else:
        return "Could not find the date difference.\n"

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
    meta_list = [meta.s_pub, meta.a_pub, meta.t_pub, meta.l_pub]

    if wayback.wayback_time:
        print("\n======== Wayback =======")
        print(wayback.wayback_time)
        print("========================")
        print(find_date(wayback.wayback_time))
    else:
        print("\n========= Meta =========")
        temp = None
        nd_counter = 0
        for i in meta_list:
            if i is not None:
                nd_counter += 1
                temp = i
                print(i)
                break
        if nd_counter == 0:
            print("Metadata: n.d. (No Date)")
        print("========================")
        print(find_date(temp))

if __name__ == "__main__":
    find_pub()
