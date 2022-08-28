# Maintainer: Leonidas P. <jpegxguy at outlook dot com>
# Maintainer: Jerry <isjerryxiao at outlook dot com>
# Contributor: Anes Belfodil <ans.belfodil at gmail dot com>
# Contributor: David Rheinsberg <david.rheinsberg at gmail dot com>
# Contributor: David Herrmann <dh.herrmann at gmail dot com>

_pkgname=qemu-user-static
_pkgver="7.0"
_pkgadditver="+dfsg-7+b1"
pkgname=${_pkgname}-bin
pkgver=${_pkgver//\~/}
pkgrel=6
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

sha256sums_x86_64=("e7b0907ec00c8f467052561464b75f7d8677acdf59e1dbfb8b1f8297a48d0178")
sha256sums_i686=("7cd79f0600890c493e8ee93b48260b894d6495bfc7706f9a2f46c3be8ac79030")
sha256sums_aarch64=("bf876c6ac33cd397cda85503ee3f7f5a69cde4c96004dd664426bb8c5d8f3b08")
sha256sums_armv7h=("3b417b6278f099ec4b8cad20ac97d25566ed77b31df11e1e6a70f4c9ecb3dc5c")
sha256sums_armv6h=("f646cc6a3873d606a4cf6247cef0191af30ffc1ce88596db5500c6e418cce7a1")

package() {
	tar -C "${pkgdir}" -xf "${srcdir}/data.tar.xz" --exclude=./usr/share/man/man1/qemu-debootstrap.1.gz ./usr/bin ./usr/share/man
}
