#!/bin/sh
git rm --cached -f $(git ls-files --exclude `basename $0`)
git add $0 lilac.py
sources=$(wget -q -O - https://github.com/archlinuxcn/repo/tree/master/$1 | sed -n '/<td class="content">/{n;s/.*<a [^>]*>\([^<]*\)<.*/\1/;p}')
for i in $sources
do
	[ $i == 'lilac.py' ] && continue
	wget -q -O $i https://raw.githubusercontent.com/archlinuxcn/repo/master/$1/$i
	git add $i
done
