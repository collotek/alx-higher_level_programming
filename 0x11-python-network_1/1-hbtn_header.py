#!/usr/bin/python3
"""A script taking in a URL, sends a request and display the value
in the X-Request-Id variable found in the header"""

if __name__ == '__main__':
    import sys
    import urllib.request
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        url_response = response.info()
        print(url_response['X-Request-Id'])
