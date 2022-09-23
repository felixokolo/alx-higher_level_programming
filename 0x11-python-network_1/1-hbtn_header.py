#!/usr/bin/python3
""" script that prints the value of the X-Request-Id
    variable found in the header of the response.
"""
if __name__ == "__main__":
    import urllib.request
    import sys
    with urllib.request.urlopen(
            sys.argv[1]) as response:
        html = response.read()
    print(("Body response:\n\t- type: {}\n" +
           "\t- content: {}\n" +
           "\t- utf8 content: {}").
          format(type(html),
                 html,
                 html.decode("utf8", "replace")))
