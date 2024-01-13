#!/bin/sh
[ -z "$2" ] && echo $0 source destination && exit

mv $1 $2

files=$(grep -rIl "\- $1" $(find . -name cactus.yaml))
for file in $files
do
	echo $file
	sed "s|- $1|- $2|g" -i $file
done
