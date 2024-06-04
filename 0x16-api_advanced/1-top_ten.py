#!/usr/bin/python3
""" A script that returns the titles of the first 10 hot posts listed
for a given subreddit
"""
import requests


def top_ten(subreddit):
    """it returns the titles of the first 10 hot posts listed"""

    resp = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "Mozilla/5.0"},
        params={"limit": 10},
    )

    if resp.status_code == 200:
        for new_data in resp.json().get("data").get("children"):
            data = new_data.get("data")
            t = data.get("title")
            print(t)
    else:
        print(None)
