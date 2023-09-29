#!/usr/bin/python3

from urllib.request import urlopen
import sys

if __name__ == "__main__":
    try:
        url = sys.argv[1]
        with urlopen(url) as resp:
            x_request_id = resp.getheader("X-Request-Id")
            print(x_request_id)
    except Exception as e:
        print(f"An error occurred: {e}")
