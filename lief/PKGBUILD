# Maintainer: Dobroslaw Kijowski [dobo] <dobo90_at_gmail.com>

pkgname=lief
pkgver=0.9.0
pkgrel=1
pkgdesc='Library to instrument executable formats'
arch=(i686  x86_64)
url='https://lief.quarkslab.com/'
license=(APACHE)
depends=(python)
makedepends=(git cmake python-setuptools)
source=("git+git://github.com/lief-project/LIEF#tag=${pkgver}")
md5sums=(SKIP)

build() {
  cd "${srcdir}/LIEF"

  mkdir build
  cd build

  cmake -DCMAKE_BUILD_TYPE=Release ..
  make

  cd "${srcdir}/LIEF/build/api/python"
  python setup.py build
}

package() {
  cd "${srcdir}/LIEF/build"
  make DESTDIR="${pkgdir}" install

  cd "${srcdir}/LIEF/build/api/python"
  python setup.py install --root="${pkgdir}" --optimize=1
}
