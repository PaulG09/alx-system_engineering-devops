#!/usr/bin/python3
import requests

"""
function that queries the Reddit API
Prints the first 10 of the hot lists
"""


def top_ten_subreddit(subreddit):

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    response = requests.get(url, headers={"User-Agent": "My Reddit Bot"})

    if response.status_code == 200:
        data = response.json()
        for post in data["data"]["children"]:
            print(post["data"]["title"])
        else:
            print("None")
