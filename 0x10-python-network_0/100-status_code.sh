#!/bin/bash
# a Bash script that sends a request to a URL passed as an argument, and displays only the status code of the response.
curl -Is $1 | grep "HTTP/1.1" | cut -d " " -f 2
