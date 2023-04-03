 #!/usr/bin/python3

"""This script fetches https://intranet.hbtn.io/status
    using the urllib package"""


import urllib.request

if __name__ == "__main__":

    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        details = response.read()

        print("Body response:")
        print("\t- type: {}".format(type(details)))
        print("\t- content: {}".format(details))
        print("\t- utf8 content: {}".format(details.decode('utf-8')))
