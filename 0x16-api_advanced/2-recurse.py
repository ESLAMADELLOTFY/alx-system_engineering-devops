#!/usr/bin/python3
"""Recursive function that queries the Reddit API for hot post titles"""
import requests
import sys
after = None


def recurse(subreddit, hot_list=[]):
    """
    Args:
        subreddit: Subreddit name.
        hot_list: List of hot titles in the subreddit.
        
    Returns:
        A list containing the titles of all hot articles for the subreddit,
        or None if the queried subreddit is invalid.
    """
    global after
    headers = {'User-Agent': 'xica369'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    parameters = {'after': after}
    response = requests.get(url, headers=headers, allow_redirects=False, params=parameters)

    if response.status_code == 200:
        data = response.json().get('data', {})
        after = data.get('after')

        list_titles = data.get('children', [])
        for title_ in list_titles:
            hot_list.append(title_.get('data', {}).get('title'))

        if after is not None:
            return recurse(subreddit, hot_list)
        return hot_list
    else:
        return None
