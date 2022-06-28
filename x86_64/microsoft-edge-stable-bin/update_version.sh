#!/bin/bash

# This script updates the package version if a new version is available

set -euxo pipefail

# Pull latest changes
git pull

# Get channel
CHANNEL=$(awk -F '=' '/^_channel/{ print $2 }' PKGBUILD)
PKG="microsoft-edge-${CHANNEL}"

# Get latest version
VER=$(curl -sSf https://packages.microsoft.com/repos/edge/dists/stable/main/binary-amd64/Packages |
    grep -A6 "Package: ${PKG}" |
    awk '/Version/{print $2}' |
	cut -d '-' -f1 |
    head -n1)

# Insert latest version into PKGBUILD and update hashes
sed -i \
    -e "s/^pkgver=.*/pkgver=${VER}/" \
    PKGBUILD

# Check whether this changed anything
if (git diff --exit-code PKGBUILD); then
    echo "Package ${PKG} has most recent version ${VER}"
    exit 0
fi

# updpkgsums
SUM256=$(curl -sSf https://packages.microsoft.com/repos/edge/dists/stable/main/binary-amd64/Packages |
    grep -A15 "Package: ${PKG}" |
    awk '/SHA256/{print $2}' |
    head -n1)

# Insert latest shasum into PKGBUILD and update hashes
sed -i \
    -e "s/^sha256sums=('.*/sha256sums=('${SUM256}'/" \
    PKGBUILD

# Reset pkgrel
sed -i \
    -e 's/pkgrel=.*/pkgrel=1/' \
    PKGBUILD

# Preparing arch-chroot
CHROOT=$HOME/.local/share/chroot
if [[ ! -d "$CHROOT" ]]; then
    mkdir -p ~/.local/share/chroot
    mkarchroot $HOME/.local/share/chroot/root base-devel
    arch-nspawn $HOME/.local/share/chroot/root pacman -Syu
fi

# Update .SRCINFO
makechrootpkg -c -r $CHROOT -- --printsrcinfo >.SRCINFO

# Start generate package
makechrootpkg -c -r $CHROOT -- -Acsf .

# Commit changes
git add PKGBUILD .SRCINFO
git commit -s -m "Update ${PKG} to v${VER}"
