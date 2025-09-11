#!/bin/bash

repo=registry.jxit.net.cn:5000/deeptalk/deeptalk-embedding

ver=$(git log --oneline . | wc -l)

docker build . -t $repo:git-$ver
# docker build . --build-arg "http_proxy=http://127.0.0.1:7890" --build-arg "https_proxy=http://127.0.0.1:7890" -t $repo:git-$ver

docker push $repo:git-$ver
