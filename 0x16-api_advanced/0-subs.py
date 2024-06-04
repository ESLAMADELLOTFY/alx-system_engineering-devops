#!/usr/bin/python3
""" Function that queries the Reddit API """
import requests
import sys


def number_of_subscribers(subreddit):
    """  
    Args:
        subreddit: subreddit name
    Returns:
        number of subscribers to the subreddit,
        or 0 if subreddit requested is invalid
    """
    headers = {'User-Agent': 'xica369'}
    # Using an f-string for URL formatting
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the request was successful
    if response.ok:
        data = response.json().get("data", {})
        return data.get("subscribers", 0)
    return 0
