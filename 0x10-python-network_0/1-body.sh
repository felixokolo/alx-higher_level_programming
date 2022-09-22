#!/bin/bash
# Gets the size of the body
response=$(curl -sI "$1")
c=$(echo $response | grep 'HTTP' | awk '{print $2}')
if ((c == 200))
then
	curl -s "$1" -X GET -L 
fi
