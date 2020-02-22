#!/usr/bin/env bash

docker ps -a | grep django | cut -f 1 -d ' ' > /tmp/cont.txt

for i in `cat /tmp/cont.txt` ; do docker rm $i; done

