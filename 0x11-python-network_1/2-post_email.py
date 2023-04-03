#!/usr/bin/python3
import urllib.request
import sys

if __name__ == '__main__':
    # Get URL and email from command line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Encode the email parameter
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    # Send the POST request and read the response
    with urllib.request.urlopen(url, data=data) as response:
        html = response.read()

    # Decode the response and print it
    print(html.decode('utf-8'))

