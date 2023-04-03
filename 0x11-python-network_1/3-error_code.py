#!/usr/bin/python3
"""
This script sends a request to the passed URL and displays the body of the response
(decoded in utf-8). If there is an HTTP error, it prints the HTTP status code.
"""

import sys
import urllib.request
import urllib.error

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
