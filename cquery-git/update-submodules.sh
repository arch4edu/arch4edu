#!/bin/bash
gitname=$1
[ -z "$2" ] && branch=master || branch=$2

[ ! -d $gitname ] && makepkg --verifysource && rmdir src

cd $gitname

if [ `git config --get core.bare` == "true" ]
then
	mkdir .git
	mv * .git
	git config --local --bool core.bare false
	git checkout $branch
fi

git reset --hard HEAD~1
git pull origin $branch
git submodule update --init

for i in `git submodule status | awk '{print $2}'`
do
	git config --file=.gitmodules submodule.$i.url "$(realpath .)/$i"
done

git add .
git commit -m 'makepkg'
