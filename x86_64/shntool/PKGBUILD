# Maintainer: envolution
# Contributor: schuay <jakob.gruber@gmail.com>
# Contributor: Michal Hybner <dta081@gmail.com>
# shellcheck shell=bash disable=SC2034,SC2154

pkgname=shntool
pkgver=3.0.10
pkgrel=8
pkgdesc="A multi-purpose WAVE data processing and reporting utility"
arch=('x86_64')
url="http://shnutils.freeshell.org/shntool/"
license=('GPL-2.0-only')
options=(!emptydirs)
depends=('glibc')
optdepends=('mac: support for ape format'
            'flac: support for flac format'
            'wavpack: support for wv format')
source=("http://shnutils.freeshell.org/shntool/dist/src/${pkgname}-${pkgver}.tar.gz"
        'debian_patches_950803.patch'
        'debian_patches_no-cdquality-check.patch'
        'shntool-3.0.10-large-size.diff'
        'shntool-3.0.10-large-times.diff')
sha256sums=('74302eac477ca08fb2b42b9f154cc870593aec8beab308676e4373a5e4ca2102'
            '2982c4c030409f2de035b7a833048692440ec9f3445b42326e7e386caa5c9e66'
            'fc5b6b0138cb2ff492f074d8c58c1bd8f562d8dee2e536d45d9098bffc0f44e3'
            '605f2030112e1ed6b68001d97a2ea839b00328995bbd795850fb2595f5797c68'
            '418f9cc575e9d9964ee85819b5db7b38108d2b19a32459ad5e9b5c19d5296292')


# Patches taken from https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=684600
# https://salsa.debian.org/debian/shntool/-/tree/master/debian/patches

prepare() {
	cd "${srcdir}"/${pkgname}-${pkgver}
  patch -Np1 < "${srcdir}/debian_patches_950803.patch"
  patch -Np1 < "${srcdir}/shntool-3.0.10-large-size.diff"
  patch -Np1 < "${srcdir}/shntool-3.0.10-large-times.diff"
  patch -Np1 < "${srcdir}/debian_patches_no-cdquality-check.patch"
}

build() {
  export CFLAGS="$CFLAGS -std=gnu99"
	cd "${srcdir}"/${pkgname}-${pkgver}
	./configure --prefix=/usr
	make
}

package() {
	cd "${srcdir}"/${pkgname}-${pkgver}
	make DESTDIR="${pkgdir}" install
}

# vim:set ts=2 sw=2 et:
