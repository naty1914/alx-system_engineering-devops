#!/usr/bin/python3
""" A script that uses the recursive function that queries the Reddit API,
parses the title of all hot articles, and prints a sorted count """
import requests


def count_words(subreddit, word_list, after='', counts={}):
    """ it returns a dictionary of word counts for a given subreddit.
    """
    if not counts:
        for word in word_list:
            if word.lower() not in counts:
                counts[word.lower()] = 0

    if after is None:
        wordict = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word in wordict:
            if word[1]:
                print('{}: {}'.format(word[0], word[1]))
        return None

    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    header = {'user-agent': 'Mozilla/5.0'}
    parameters = {'limit': 100, 'after': after}
    resp = requests.get(url, headers=header, params=parameters,
                        allow_redirects=False)

    if resp.status_code != 200:
        return None
    try:
        hot = resp.json()['data']['children']
        after = resp.json()['data']['after']
        for post in hot:
            title = post['data']['title']
            lower = [word.lower() for word in title.split(' ')]
            for word in counts.keys():
                counts[word] += lower.count(word)
    except Exception:
        return None
    count_words(subreddit, word_list, after, counts)
