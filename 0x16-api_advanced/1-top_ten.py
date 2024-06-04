#!/usr/bin/python3
""" Function that queries the Reddit API """
import requests
import sys


def top_ten(subreddit):
    """
    Fetches and prints the top ten post titles from a given subreddit.
    
    Args:
        subreddit: The name of the subreddit to query.
        
    Returns:
        None. Prints the titles of the top ten posts or "None" if the subreddit is invalid.
    """
    headers = {'User-Agent': 'xica369'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    parameters = {'limit': 10}
    response = requests.get(url, headers=headers, allow_redirects=False, params=parameters)

    # Verify if the request was successful
    if response.ok:
        # Extract the list of top 10 posts
        titles_ = response.json().get('data', {}).get('children', [])
        for title_ in titles_:
            # Display the title of each post
            print(title_.get('data', {}).get('title'))
    else:
        # Output None if the subreddit is invalid
        print(None)
