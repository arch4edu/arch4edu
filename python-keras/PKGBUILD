# Maintainer: Fabien Dubosson <fabien.dubosson@gmail.com>
# Contributer: David McInnis <davidm@eagles.ewu.ewu>

pkgbase="python-keras"
pkgname=("python-keras" "python2-keras")
_pkgname="keras"
pkgver="2.0.0"
pkgrel="1"
pkgdesc="Deep Learning library (convnets, recurrent neural networks, and more)"
arch=('any')
url="https://github.com/fchollet/keras"
license=('MIT')
makedepends=('python' 'python-setuptools' 'python-numpy' 'python-scipy' 'python-h5py'
             'python2' 'python2-setuptools' 'python2-numpy' 'python2-scipy' 'python2-h5py'
            )
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/fchollet/${_pkgname}/archive/${pkgver}.tar.gz")
sha256sums=('1cfe5c298be813a512549f993e4d4fdfe0f887a8e67f7bf915fda6089ac9d403')

prepare() {
  cd "$srcdir/"
  cp -a "${_pkgname}-${pkgver}" "${_pkgname}-${pkgver}-py2"
  cd "${_pkgname}-${pkgver}"
  sed -e "s|#![ ]*/usr/bin/python$|#!/usr/bin/python2|" \
      -e "s|#![ ]*/usr/bin/env python$|#!/usr/bin/env python2|" \
      -e "s|#![ ]*/bin/env python$|#!/usr/bin/env python2|" \
      -i $(find . -name '*.py')
}

build() {
  msg "Building Python 2"
  cd "$srcdir/${_pkgname}-${pkgver}-py2"
  python2 setup.py build

  msg "Building Python 3"
  cd "$srcdir/${_pkgname}-${pkgver}"
  python setup.py build
}

package_python2-keras() {
  depends=('python2' 'python2-numpy' 'python2-scipy' 'python2-h5py')
  optdepends=('python2-theano')
  cd "$srcdir/${_pkgname}-${pkgver}-py2"
  python2 setup.py install --root="$pkgdir"/ --optimize=1
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE.txt"
}

package_python-keras() {
  depends=('python' 'python-numpy' 'python-scipy' 'python-h5py')
  optdepends=('python-theano' 'python-tensorflow')
  cd "$srcdir/${_pkgname}-${pkgver}"
  python setup.py install --root="$pkgdir"/ --optimize=1
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE.txt"
}

# vim:set ts=2 sw=2 et:
