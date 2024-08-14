#!/usr/bin/python3
"""fetch reddit API and get number os subscribers"""
import requests


def number_of_subscribers(subreddit):
    """return number of subscribers for each subreddit
    or 0 if the subreddit if not found"""
    url_api = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {"User-Agent": "My-User-Agent"}
    response = requests.get(url_api, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
