# Maintainer: David McInnis <dave@dave3.xyz>
# Contributer: Fabien Dubosson <fabien.dubosson@gmail.com>

pkgbase="python-keras"
pkgname=("python-keras" "python2-keras")
_pkgname="keras"
pkgver="2.2.2"
pkgrel=3
pkgdesc="Deep Learning library (convnets, recurrent neural networks, and more)"
arch=('any')
url="https://github.com/fchollet/keras"
license=('MIT')
makedepends=('python-setuptools' 'python-numpy'  'python-scipy'  'python-h5py'  'python-yaml'
             'python2-setuptools' 'python2-numpy' 'python2-scipy' 'python2-h5py' 'python2-yaml'
            )
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/fchollet/${_pkgname}/archive/${pkgver}.tar.gz")
sha256sums=('76a7110a0f7b6114bfcf9453057a7e3c65e3957791336423b09a7420fc3de3a8')

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
  depends=('python2' 'python2-numpy' 'python2-scipy' 'python2-h5py' 'python2-yaml')
  optdepends=('python2-theano' 'cudnn'
              'python2-keras-applications: Must Install for python2-keras to work!'
              'python2-keras-preprocessing: Must Install for python2-keras to work!')
  cd "$srcdir/${_pkgname}-${pkgver}-py2"
  python2 setup.py install --root="$pkgdir"/ --optimize=1
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE.txt"
}

package_python-keras() {
  depends=('python' 'python-numpy' 'python-scipy' 'python-h5py' 'python-yaml')
  optdepends=('python-theano' 'python-tensorflow' 'cudnn'
              'python-keras-applications: Must Install for python-keras to work!'
              'python-keras-preprocessing: Must Install for python-keras to work!')
  cd "$srcdir/${_pkgname}-${pkgver}"
  python setup.py install --root="$pkgdir"/ --optimize=1
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE.txt"
}

