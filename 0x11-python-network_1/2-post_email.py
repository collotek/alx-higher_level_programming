#!/usr/bin/python3
"""Python script takes in a URL and an email,
sends a POST request to passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)"""


if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys

    passed_url = sys.argv[1]
    passed_email = {'email': sys.argv[2]}
    email = urllib.parse.urlencode(passed_email)
    email = email.encode('ascii')
    url_req = urllib.request.Request(passed_url, email)

    with urllib.request.urlopen(url_req) as response:
        url_res = response.read()
    output = url_res.decode('utf-8')
    print(output)
