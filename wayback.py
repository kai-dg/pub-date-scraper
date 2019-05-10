#!/usr/bin/env python3
"""
Contains functions for interfacing with Wayback API.
"""

import datetime
import json
import requests


class Wayback:
    """Class containing wayback data"""

    def __init__(self, url):
        self.url = url
        self.wayback_time = self.call_wayback()

    def string_to_time(self, string):
        """
        Converts string to datetime object.
        """
        return datetime.datetime.strptime(string, '%Y%m%d%H%M%S')


    def call_wayback(self):
        """
        Returns the oldest recorded date of a link's existence in Wayback.
        """
        domain = 'http://archive.org'
        query = '/wayback/available?'
        payload = {}
        payload['url'] = self.url
        # Wayback only lets you get the closest snapshot of a specified time
        # so we get the closest to the 'beginning of time' aka. the oldest
        payload['timestamp'] = '00000000000000'
        r = requests.get(domain + query, params=payload)
        r.raise_for_status()
        try:
            timestamp = r.json()['archived_snapshots']['closest']['timestamp']
        except KeyError:
            # Will experience KeyError when no entry in Wayback exists.
            return None
        return self.string_to_time(timestamp)

if __name__ == '__main__':
    url = 'https://www.allrecipes.com/recipe/20334/banana-pancakes-i/'
    d = call_wayback(url)
    print(d)
