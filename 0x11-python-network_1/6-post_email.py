#!/usr/bin/python3
"""
This script takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter, and displays the response body.
"""

import requests
import sys

if __name__ == "__main__":
    url, email = sys.argv[1], sys.argv[2]
    response = requests.post(url, data={'email': email})
    print(response.text)
