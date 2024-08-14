#!/usr/bin/python3
"""fetch hot posts from reddit API"""
import requests


headers = {"User-Agent": "My-User-Agent"}


def top_ten(subreddit):
    """fetch and print 10 hot posts on reddit using reddit API"""
    params = {
        'limit': 8,
    }
    api_url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    response = requests.get(api_url,
                            headers=headers,
                            params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        if len(posts) == 0:
            print(None)
        titles = []
        for post in posts:
            post_data = post['data']
            titles.append(post_data['title'])
        titles.sort()
        for title in titles:
            print(title)
    else:
        print(None)
