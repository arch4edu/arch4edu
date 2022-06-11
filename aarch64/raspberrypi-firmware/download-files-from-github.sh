#!/bin/sh
set -e
repo=$1
path=$2

git rm --cached -f $(git ls-files --exclude `basename $0`)
for i in $0 lilac.py lilac.yaml package.list
do
	git add $i || :
done

sources=$(wget -q -O - https://api.github.com/repos/$repo/contents/$path | jq -r '.[] | select(.type=="file") | .name')

for i in $sources
do
	echo Downloading $i
	wget -q -O $i https://raw.githubusercontent.com/$1/master/$2/$i
	git add $i
done
