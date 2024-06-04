#!/usr/bin/python3
""" A script that returns the number of subscribers for a given subreddit"""
import requests


def number_of_subscribers(subreddit):
    """it returns the number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    resp = requests.get(url, headers=headers, allow_redirects=False)
    if resp.status_code == 200:
        data = resp.json()
        return data['data']['subscribers']
    else:
        return 0
