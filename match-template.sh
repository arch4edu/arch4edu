#!/bin/sh
[ -z "$1" ] && path='.' || path=$1

files=$(find $path -type f -name cactus.yaml)

for file in $files
do
	for template in template/*
	do
		cmp --silent $file $template && rm $file && ln -s $(realpath --relative-to=$(dirname $file) $template) $file && echo "$template -> $file"
	done
done
