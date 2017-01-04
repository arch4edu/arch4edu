#!/bin/sh
sources=$(wget -q -O - https://github.com/archlinuxcn/repo/tree/master/$1 | sed -n '/<td class="content">/{n;s/^.*<a href="[^"]*\/\([^"\/]*\)".*$/\1/;p}')
git add $0
for i in $sources
do
	[ $i == 'lilac.py' ] && continue
	wget -q -O $i https://raw.githubusercontent.com/archlinuxcn/repo/master/$1/$i
	git add $i
done
