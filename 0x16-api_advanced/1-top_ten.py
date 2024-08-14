#!/usr/bin/python3
"""fetch hot posts from reddit API"""
import requests


def top_ten(subreddit):
    """fetch and print 10 hot posts on reddit using reddit API"""
    api_url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for index in range(10):
            post = posts[index]
            post_data = post['data']
            title = post_data['title']
            print(title)
