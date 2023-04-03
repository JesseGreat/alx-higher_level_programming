#!/usr/bin/python3

"""
This script fetches https://alx-intranet.hbtn.io/status
using the urllib package.
"""

import urllib.request


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        details = response.read()

    print("Body response:")
    print(f"\t- type: {type(details)}")
    print(f"\t- content: {details}")
    print(f"\t- utf8 content: {details.decode('utf-8')}")
