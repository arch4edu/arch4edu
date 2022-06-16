# Maintainer: Jingbei Li <i@jingbei.li>
# Contributor: Benjamin Chretien <chretien at lirmm dot fr>
# Contributor: Sebastien Binet <binet@lblbox>

pkgname=python-pybindgen
_pkgname='PyBindGen'
pkgver=0.22.1
pkgrel=1
pkgdesc="A tool to generate Python bindings for C/C++ code"
url='https://github.com/gjcarneiro/pybindgen'
arch=('i686' 'x86_64')
license=('LGPL')
depends=('python')
makedepends=('python-setuptools' 'python-pip')
# Note: pygccxml does not support Python 3 yet
#optdepends=('gccxml' 'pygccxml')
source=("https://pypi.python.org/packages/source/P/PyBindGen/PyBindGen-${pkgver}.tar.gz")
md5sums=('a082555346450f008d68c337c2e175d0')

build() {
  cd ${srcdir}/${_pkgname}-$pkgver
  python setup.py build
}

package() {
  cd ${srcdir}/${_pkgname}-$pkgver
  python setup.py install --root="$pkgdir"/ --optimize=1
}
