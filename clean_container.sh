#!/usr/bin/env bash

## The script clears all containers that has django in the listing

## Once can get the same affect by running: docker-compose down

docker ps -a | grep django | cut -f 1 -d ' ' > /tmp/cont.txt

for i in `cat /tmp/cont.txt` ; do docker rm $i; done

## Also clear the images that are not tagged.  Listing has <none>

docker images | grep "<none>" | cut -c 58-70 > /tmp/img.txt

for i in `cat /tmp/img.txt`; do docker rmi $i; done

