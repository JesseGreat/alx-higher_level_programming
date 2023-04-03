#!/usr/bin/python3


"""This script fetches a header from https://intranet.hbtn.io/status"""

import requests
import sys

if __name__ == '__main__':
    # get URL from command line arguments
    url = sys.argv[1]

    # send a request to the URL and get the response
    response = requests.get(url)

    # check if the response contains the X-Request-Id header
    if 'X-Request-Id' in response.headers:
        # if it does, print the value of the header
        print(response.headers['X-Request-Id'])
    else:
        print("X-Request-Id header not found in the response")
