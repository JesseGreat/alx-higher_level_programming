#!/usr/bin/python3

"""This script sends a POST request to the passed URL
    with the email as a parameter,
    and displays the body of the response (decoded in utf-8)"""

import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    # Get the URL and email from command line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Encode the email as a URL parameter
    params = urllib.parse.urlencode({'email': email}).encode('utf-8')

    # Send a POST request to the URL with the email as a parameter
    with urllib.request.urlopen(url, data=params) as response:
        # Read and decode the response body in utf-8
        body = response.read().decode('utf-8')

    # Print the response body
    print(body)

