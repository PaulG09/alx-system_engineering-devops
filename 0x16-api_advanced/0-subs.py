#!/usr/bin/python3

def number_of_subscribers(subreddit):

    """
    Queries the Reddit API and returns the number of subscribers for a
    given subreddit
    If the subreddit is invalid, the function returns 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agents": "myApp/0.0.1"}

    try:
        # Make the requests with no redirect
        response = requests.get(url, headers=headers, allow_redirects=False)
        # Check if the response was successful
        if response.status_code == 200:
            data = response.json()
            return data['data'].get('subscribers', 0)
        else:
            return 0
    except requests.RequestException:
        return 0
