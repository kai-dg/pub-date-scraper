#!/usr/bin/env python3
"""
Contains function for scraping and formatting a website's date.
"""

import dateutil.parser
from datetime import datetime, timezone

from helpers.log import log


def iso_to_date(iso_str):
    """
    Converts ISO date format to datetime object.
    """
    return dateutil.parser.parse(iso_str)


def scrape_date(soup):
    """
    Scrapes the publication date of a website using time HTML tag.
    """
    log("Scraping publication date.")
    # This is a backup in the case of Wayback not having a record
    pub_date = soup.find('time')
    if pub_date is None:
        return None
    pub_date = pub_date.get('datetime')
    pub_date = iso_to_date(pub_date)
    # Get rid of timezone info
    pub_date = pub_date.replace(tzinfo=None)
    return pub_date
