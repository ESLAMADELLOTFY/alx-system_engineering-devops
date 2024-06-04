#!/usr/bin/python3
"""Recursive function that queries the Reddit API"""
import requests
import sys

# Global variables to manage pagination and counting
after = None
count_dic = []


def count_words(subreddit, word_list):
    """
    Parses the titles of all hot articles and prints a sorted count of given
    keywords (case-insensitive, delimited by spaces).

    Args:
        subreddit (str): The name of the subreddit to query.
        word_list (list): List of keywords to count in the titles.

    Returns:
        None. Prints the count of each keyword found in the titles of hot articles.
    """
    global after
    global count_dic

    headers = {'User-Agent': 'xica369'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    parameters = {'after': after}
    
    response = requests.get(url, headers=headers, allow_redirects=False, params=parameters)
    
    if response.status_code == 200:
        data = response.json().get('data', {})
        after = data.get('after')

        # Extract and process titles of hot posts
        list_titles = data.get('children', [])
        for title_ in list_titles:
            title = title_.get('data', {}).get('title', "").lower()
            for word in word_list:
                if word.lower() in title:
                    count_dic.append(word.lower())

        # Continue pagination if there are more posts
        if after is not None:
            count_words(subreddit, word_list)
        else:
            # Count occurrences of each word in the list
            word_count = {}
            for word in word_list:
                word_count[word.lower()] = count_dic.count(word.lower())
            
            # Sort and print the word counts
            sorted_word_count = sorted(word_count.items(), key=lambda item: (-item[1], item[0]))
            for word, count in sorted_word_count:
                if count > 0:
                    print(f"{word}: {count}")
    else:
        print(None)
