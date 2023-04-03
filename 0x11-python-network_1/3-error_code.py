#!/usr/bin/env python3

"""
This script sends a request to the passed URL and displays the body of the response
(decoded in utf-8). If there is an HTTP error, it prints the HTTP status code.
"""

import sys
import urllib.request
import urllib.error

if __name__ == '__main__':
    # Get the URL from the command line arguments
    url = sys.argv[1]

    try:
        # Send a request to the URL and get the response
        with urllib.request.urlopen(url) as response:
            # Decode the response body and print it
            print(response.read().decode('utf-8'))

    except urllib.error.HTTPError as e:
        # If an HTTP error occurs, print the HTTP status code
        print(f"Error code: {e.code}")

