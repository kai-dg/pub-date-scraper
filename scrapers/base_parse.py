#!/usr/bin/env python3
"""
Contains class responsible for sending GET request and saving data about URL.
"""

import requests
from bs4 import BeautifulSoup

import settings


class BaseParse:
    """
    Sends GET request to URL, saves response code and parsed HTML (soup).
    """

    def __init__(self, url):
        self.url = url
        self.soup = self.make_soup()

    def make_soup(self):
        """
        Makes request and parses HTML with BeautifulSoup.
        """
        response = requests.get(self.url, headers=settings.headers)
        self.status = response.status_code
        html = response.content
        return BeautifulSoup(html, 'html.parser')
