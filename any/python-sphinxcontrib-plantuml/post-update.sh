#!/bin/bash

set -exuo pipefail

uid="$(id -u)"

# Move pkgrel back to 1 after a version bump
sed -i 's/pkgrel=.*/pkgrel=1/' ./PKGBUILD

# Update checksums and the .SRCINFO file to match the new version.
# The easiest and most consistent way to do this is by using the
# archlinux-provided tools for this. Because renovate doesn't run in an arch
# container, use docker to spin up a temporary container for this purpose.
# makepkg in this container cannot be run as root. Therefore, create a
# temporary user for this. This used need to use the UID of the host's user to
# avoid file access problems when using bind mounts in docker.
docker run --rm -v "$(pwd):/pkg" archlinux:latest bash -c "
set -exuo pipefail
pacman -Syu --noconfirm pacman-contrib binutils
useradd -u ${uid} builder
cd /pkg
su builder -c updpkgsums
su builder -c 'makepkg --printsrcinfo > .SRCINFO'
"
