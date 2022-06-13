# Maintainer: Leonidas P. <jpegxguy at outlook dot com>
# Maintainer: Jerry <isjerryxiao at outlook dot com>
# Contributor: Anes Belfodil <ans.belfodil at gmail dot com>
# Contributor: David Rheinsberg <david.rheinsberg at gmail dot com>
# Contributor: David Herrmann <dh.herrmann at gmail dot com>

_pkgname=qemu-user-static
_pkgver="7.0"
_pkgadditver="+dfsg-7"
pkgname=${_pkgname}-bin
pkgver=${_pkgver//\~/}
pkgrel=5
pkgdesc='A generic and open source machine emulator, statically linked'
arch=('x86_64' 'i686' 'aarch64' 'armv7h' 'armv6h')
url="http://wiki.qemu.org"
license=('GPL2' 'LGPL2.1')
depends=('binfmt-qemu-static')
provides=("qemu-user" "${_pkgname}" "qemu-arm-static")
conflicts=("qemu-user" "${_pkgname}" "qemu-arm-static")

source_x86_64=("https://deb.debian.org/debian/pool/main/q/qemu/${_pkgname}_${_pkgver}${_pkgadditver}_amd64.deb")
source_i686=("https://deb.debian.org/debian/pool/main/q/qemu/${_pkgname}_${_pkgver}${_pkgadditver}_i386.deb")
source_aarch64=("https://deb.debian.org/debian/pool/main/q/qemu/${_pkgname}_${_pkgver}${_pkgadditver}_arm64.deb")
source_armv7h=("https://deb.debian.org/debian/pool/main/q/qemu/${_pkgname}_${_pkgver}${_pkgadditver}_armhf.deb")
source_armv6h=("https://deb.debian.org/debian/pool/main/q/qemu/${_pkgname}_${_pkgver}${_pkgadditver}_armel.deb")

sha256sums_x86_64=("2442512d3233ae2935097d0385138b813fdb07ad440bfacb7bc6996f827e5fd9")
sha256sums_i686=("291b9024c1809414d92cc13894b31c6ee61e1240a67db01374f7aeebb8567610")
sha256sums_aarch64=("a7a71b848d1ef8194e68fac7aebb5394949a95d2584dfe0667184323530fefdc")
sha256sums_armv7h=("eac9dc4812ea0e618d4abf5edf6b913191b35b2ad802bf66e4a3bb8618c13b66")
sha256sums_armv6h=("fa470f2cf6ed6b7095327223a1c292a6d7459bd30c7e6043297f0fbedea3bd9d")

package() {
	tar -C "${pkgdir}" -xf "${srcdir}/data.tar.xz" --exclude=./usr/share/man/man1/qemu-debootstrap.1.gz ./usr/bin ./usr/share/man
}
