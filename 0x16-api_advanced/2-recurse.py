#!/usr/bin/python3
"""fetch hot posts from reddit API"""
import requests

params = {
    'limit': 100,
    'count': 0,
    'after': None
}


def recurse(subreddit, hot_list=[]):
    """fetch all hot posts"""

    api_url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    response = requests.get(api_url, params=params)
    if response.status_code != 200:
        return hot_list

    data = response.json()
    posts = data['data']['children']
    for post in posts:
        post_data = post['data']
        title = post_data['title']
        hot_list.append(title)
        print(title)

    recurse(subreddit, hot_list)
