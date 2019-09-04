# Maintainer: Benjamin Chretien <chretien at lirmm dot fr>
# Contributor: Sebastien Binet <binet@lblbox>
pkgname=python-pybindgen
pkgver=0.17.0
pkgrel=3
pkgdesc="A tool to generate Python bindings for C/C++ code"
url="http://pypi.python.org/pypi/PyBindGen"
arch=('i686' 'x86_64')
license=('LGPL')
depends=('python')
# Note: pygccxml does not support Python 3 yet
#optdepends=('gccxml' 'pygccxml')
makedepends=('waf')
provides=('python-pybindgen')
conflicts=('python-pybindgen-bzr')
source=("https://pypi.python.org/packages/source/P/PyBindGen/PyBindGen-${pkgver}.tar.gz")
md5sums=('7d8fe2b3b4646c3c1d9e5342b1645f6a')

_pkgname=PyBindGen

build() {
  cd ${srcdir}/${_pkgname}-$pkgver
  PYTHON=python3 ./waf configure --prefix=/usr --disable-pygccxml
  PYTHON=python3 ./waf
}

check() {
  cd ${srcdir}/${_pkgname}-$pkgver
  PYTHON=python3 ./waf check
}

package() {
  cd ${srcdir}/${_pkgname}-$pkgver
  PYTHON=python3 ./waf install --prefix=/usr --destdir=${pkgdir}
}
