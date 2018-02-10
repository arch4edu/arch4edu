# $Id$
# Maintainer:
# Contributor: Stéphane Gaudreault <stephane@archlinux.org>
# Contributor: Thomas Dziedzic < gostrc at gmail >
# Contributor: Denis Martinez <deuns.martinez AT gmail.com>

pkgname=intel-tbb-gcc6
pkgver=2018_20171205
_pkgver=2018_U2
pkgrel=1
pkgdesc='High level abstract threading library'
arch=(x86_64)
url='http://www.threadingbuildingblocks.org/'
license=(GPL)
depends=(gcc-libs gcc6)
provides=('intel-tbb')
replaces=('intel-tbb')
conflicts=('intel-tbb')
source=(https://github.com/01org/tbb/archive/$_pkgver.tar.gz)
sha256sums=('78bb9bae474736d213342f01fe1a6d00c6939d5c75b367e2e43e7bf29a6d8eca')

build() {
  cd tbb-$_pkgver
  export CXXFLAGS+=" -fno-lifetime-dse" # FS#49898
  make CC=gcc-6 CXX=g++-6
}

package() {
  cd tbb-$_pkgver
  install -d "$pkgdir"/usr/lib
  install -m755 build/linux_*/*.so* "$pkgdir"/usr/lib
  install -d "$pkgdir"/usr/include
  cp -a include/tbb "$pkgdir"/usr/include
}
