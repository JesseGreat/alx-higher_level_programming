 #!/usr/bin/python3

 import urllib.request


    # Set the URL to fetch to a variable
    url = 'https://alx-intranet.hbtn.io/status'

    # Use the with statement to open the URL and make an HTTP request
    # The response object is automatically closed at the end of the with statement
    with urllib.request.urlopen(url) as response:
        # Read the contents of the response and assign to a variable
        html = response.read()

    # Display some information about the response received from the server
    print("Body response:")
    # Display the type of the "html" variable
    print("\t- type: {}".format(type(html)))
    # Display the content of the response as a sequence of bytes
    print("\t- content: {}".format(html))
    # Display the UTF-8 encoded content of the response as a string
    print("\t- utf8 content: {}".format(html.decode('utf-8'))))

if __name__ == "__main__":
