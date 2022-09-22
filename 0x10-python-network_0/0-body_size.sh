#!/bin/bash
# Gets the size of the body
curl -sI "$1" | grep 'Content-Length' | gawk '{print $2}'
