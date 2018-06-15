# This is an example PKGBUILD file. Use this as a start to creating your own,
# and remove these comments. For more information, see 'man PKGBUILD'.
# NOTE: Please fill out the license field for your package! If it is unknown,
# then please put 'unknown'.

# Maintainer: Oliver Harley <oliver.r.harley@gmail.com>
pkgbase=python-keras-applications
pkgname=("python-keras-applications" "python2-keras-applications")
_pkgname=keras-applications
pkgver=1.0.2
pkgrel=1
pkgdesc="Applications module of the Keras deep learning library"
arch=('any')
url="https://github.com/keras-team/keras-applications/"
license=('MIT')
makedepends=('python'  'python-setuptools'  'python-numpy'  'python-h5py'
             'python2' 'python2-setuptools' 'python2-numpy' 'python2-h5py'
             'python-keras' )
provides=(python-keras-applications)
source=("$_pkgname-$pkgver.tar.gz::https://github.com/keras-team/$_pkgname/archive/$pkgver.tar.gz")
sha256sums=('6d8923876a7f7f2d459dd7efe3b10830f316f714b707f0c136e7f00c63035338')

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

package_python2-keras-applications() {
  depends=('python2' 'python2-numpy' 'python-keras')
  optdepends=('python2-theano' 'cudnn')
  cd "$srcdir/${_pkgname}-${pkgver}-py2"
  python2 setup.py install --root="$pkgdir"/ --optimize=1
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE.txt"
}

package_python-keras-applications() {
  depends=('python' 'python-numpy' 'python-keras')
  cd "$srcdir/${_pkgname}-${pkgver}"
  python setup.py install --root="$pkgdir"/ --optimize=1
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE.txt"
}

