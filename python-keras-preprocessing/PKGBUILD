# Maintainer: Oliver Harley <oliver.r.harley+aur (at) gmail.com>
# Since python-keras pulls in quite a few dependencies and I assume few people are using python2 for
# keras (no complaints thus far), the required makedepends for the python2 version has been
# commented out, remove the comment and additional ')' if you require the python2 version.

_pkgname=keras-preprocessing
pkgbase=python-keras-preprocessing
pkgname=("python-keras-preprocessing" "python2-keras-preprocessing")
pkgver=1.0.2
pkgrel=2
pkgdesc="Preprocessing module of the Keras deep learning library"
arch=('any')
url="https://github.com/keras-team/keras-preprocessing/"
license=('MIT')
# add python2-keras to makedepends for python2 version
makedepends=('python'  'python-setuptools'  'python-numpy' 'python-keras'
             'python2' 'python2-setuptools' 'python2-numpy')  # 'python2-keras')

provides=(python-keras-preprocessing)
source=("$_pkgname-$pkgver.tar.gz::https://github.com/keras-team/$_pkgname/archive/$pkgver.tar.gz")
sha256sums=('64212b715a435b43724ecf26be67a441cee426e3ef614a6326aba06016ba9779')

prepare() {
  cd "$srcdir/"
  cp -a "${_pkgname}-${pkgver}" "${_pkgname}-${pkgver}-py2"
  cd "${_pkgname}-${pkgver}-py2"
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

package_python2-keras-preprocessing() {
  depends=('python2-numpy' 'python2-keras')
  cd "$srcdir/${_pkgname}-${pkgver}-py2"
  python2 setup.py install --root="$pkgdir"/ --optimize=1
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE.txt"
}

package_python-keras-preprocessing() {
  depends=('python-numpy' 'python-keras')
  cd "$srcdir/${_pkgname}-${pkgver}"
  python setup.py install --root="$pkgdir"/ --optimize=1
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE.txt"
}
