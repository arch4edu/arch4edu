
# This is an example PKGBUILD file. Use this as a start to creating your own,
# and remove these comments. For more information, see 'man PKGBUILD'.
# NOTE: Please fill out the license field for your package! If it is unknown,
# then please put 'unknown'.

# Maintainer: Oliver Harley <oliver.r.harley@gmail.com>
pkgbase=python-keras-preprocessing
pkgname=("python-keras-preprocessing" "python2-keras-preprocessing")
_pkgname=keras-preprocessing
pkgver=1.0.1
pkgrel=1
pkgdesc="Preprocessing module of the Keras deep learning library"
arch=('any')
url="https://github.com/keras-team/keras-preprocessing/"
license=('MIT')
makedepends=('python'  'python-setuptools'  'python-numpy'  'python-scipy' 'python-keras'
             'python-six' 'python2-six' 'python2' 'python2-setuptools' 'python2-numpy' 'python2-scipy')
provides=(python-keras-preprocessing)
source=("$_pkgname-$pkgver.tar.gz::https://github.com/keras-team/$_pkgname/archive/$pkgver.tar.gz")
sha256sums=('2e9e187afd1327d802309513cc6366d72a5c02104c6815da30d8651a4bd20699')

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

package_python2-keras-preprocessing() {
  depends=('python2' 'python2-numpy' 'python-keras' 'python2-six')
  optdepends=('python2-theano' 'cudnn')
  cd "$srcdir/${_pkgname}-${pkgver}-py2"
  python2 setup.py install --root="$pkgdir"/ --optimize=1
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE.txt"
}

package_python-keras-preprocessing() {
  depends=('python' 'python-numpy' 'python-keras' 'python-six')
  cd "$srcdir/${_pkgname}-${pkgver}"
  python setup.py install --root="$pkgdir"/ --optimize=1
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE.txt"
}
