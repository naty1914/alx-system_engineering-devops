#!/usr/bin/python3
""" A script that returns a list containing the titles of all hot articles
for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """it returns a list containing the titles of all hot articles"""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 100, 'after': after}

    resp = requests.get(url, headers=headers, params=params)
    if resp.status_code == 200:
        data = resp.json()
        c = data['data']['children']
        for child in c:
            hot_list.append(child['data']['title'])
        after = data['data']['after']
        if after:
            return recurse(subreddit, hot_list, after)
        return hot_list
    else:
        return None
