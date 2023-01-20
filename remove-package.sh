#!/bin/sh
[ -z "$1" ] && echo $0 path && exit

files=$(grep -rIl "\- $1" $(find . -name cactus.yaml))
for file in $files
do
	echo $file
	sed "/\- ${1//\//\\\/}/d" -i $file
	[ $(yq -c .depends $file) = "null" ] && sed '/^depends:/d' -i $file
	[ $(yq -c .makedepends $file) = "null" ] && sed '/^makedepends:/d' -i $file
	for template in template/*
	do
		cmp --silent $file $template && rm $file && ln -s $(realpath --relative-to=$file $template) $file
	done
done

rm -r $1
