#!/bin/sh
repo=$1
path=$2

git rm --cached -f $(git ls-files --exclude `basename $0`)
git add $0 lilac.py

sources=$(wget -q -O - https://github.com/$1/tree/master/$2 | sed -n '/<td class="content">/{n;s/.*<a [^>]*>\([^<]*\)<.*/\1/;p}')
for i in $sources
do
	wget -q -O $i https://raw.githubusercontent.com/$1/master/$2/$i
	git add $i
done
