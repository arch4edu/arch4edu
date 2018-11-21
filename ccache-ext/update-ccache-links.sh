#!/bin/sh

cd /usr/lib/ccache/bin
for file in {c++,cc,clang,clang++,g++,gcc} {c++,cc,clang,clang++,g++,gcc}-[0-9]* *-{c++,cc,clang,clang++,g++,gcc} *-{c++,cc,clang,clang++,g++,gcc}-[0-9]*
do
    if [[ -L $file ]]
    then
        rm "/usr/lib/ccache/bin/$file"
    fi
done

cd /usr/bin
for file in {c++,cc,clang,clang++,g++,gcc} {c++,cc,clang,clang++,g++,gcc}-[0-9]* *-{c++,cc,clang,clang++,g++,gcc} *-{c++,cc,clang,clang++,g++,gcc}-[0-9]*
do
    if [[ -x $file ]]
    then
        ln -s /usr/bin/ccache "/usr/lib/ccache/bin/$file"
    fi
done
