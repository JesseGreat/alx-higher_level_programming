#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the
URL, and displays the response body.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    if response.ok:
        print(response.text)
    else:
        print(f"Error code: {response.status_code}")
