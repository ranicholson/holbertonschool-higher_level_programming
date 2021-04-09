#!/usr/bin/python3
"""Script that send a reuest to enetered url and siaplays X-Request-Id"""

import sys
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(dict(response.headers).get("X-Request-Id"))
