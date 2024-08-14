#!/usr/bin/python3
"""fetch hot posts from reddit API"""
import requests


headers = {"User-Agent": "My-User-Agent"}


def recurse(subreddit, hot_list=[], after=None):
    """fetch all hot posts"""
    params = {
        'limit': 100,
        'after': after
    }
    api_url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    response = requests.get(api_url, headers=headers,
                            params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return hot_list

    data = response.json()
    posts = data['data']['children']
    for post in posts:
        post_data = post['data']
        title = post_data['title']
        hot_list.append(title)
        print(title)

    recurse(subreddit, hot_list, data['data'].get('after'))
