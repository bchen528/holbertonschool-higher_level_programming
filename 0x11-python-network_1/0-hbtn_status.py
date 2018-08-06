#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status"""
import urllib.request


if __name__ == "__main__":
    """fetches https://intranet.hbtn.io/status"""
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        html_str = html.decode('utf-8')

    print("Body response:")
    print("    - type: {}".format(type(html)))
    print("    - content: {}".format(html))
    print("    - utf8 content: {}".format(html_str))
