Archlinux Repository for Education
========
Making your Archlinux and ArchlinuxARM better for researching and developing.

### Introduction

Arch4edu is a community repository for Archlinux and ArchlinuxARM that strives to provide the latest versions of most software used by college students.

Please visit the [wiki](../../wiki) site for more information.

### Usage

Please add
```
[arch4edu]
SigLevel = Never
Server = https://mirrors.tuna.tsinghua.edu.cn/arch4edu/$arch
```
to your `/etc/pacman.conf`.

**Recommended**: Please also install `pkgstats` to help us learn the trends of the packages we maintaining.
```
$ pacman -S pkgstats
```
