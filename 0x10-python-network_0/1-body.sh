#!/bin/bash
# Gets the size of the body
response=$(curl -sI "$1")
c=$(echo $response | grep 'HTTP' | gawk '{print $2}')
if ((c == 200))
then
	echo grep '<body>' $response
fi
