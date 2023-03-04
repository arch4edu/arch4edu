# Maintainer: schuay <jakob.gruber@gmail.com>
# Contributor: Michal Hybner <dta081@gmail.com>

pkgname=shntool
pkgver=3.0.10
pkgrel=7
pkgdesc="A multi-purpose WAVE data processing and reporting utility"
arch=('x86_64')
url="http://shnutils.freeshell.org/shntool/"
license=('GPL')
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
	cd "${srcdir}"/${pkgname}-${pkgver}
	./configure --prefix=/usr
	make
}

package() {
	cd "${srcdir}"/${pkgname}-${pkgver}
	make DESTDIR="${pkgdir}" install
}

md5sums=('5d41f8f42c3c15e3145a7a43539c3eae'
         'a3aa5b817cedb4226fa32340609a5995'
         '596398b13e02b243078320ebde4743fb'
         '4265935ef1d684a4b49041278ffda7de'
         '6f0d61ddbf8cbee5c0b51a99e987ddda')

# vim:set ts=2 sw=2 et:
