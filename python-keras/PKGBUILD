# Maintainer: David McInnis <dave@dave3.xyz>
# Contributer: Fabien Dubosson <fabien.dubosson@gmail.com>

pkgbase="python-keras"
pkgname=("python-keras" "python2-keras")
_pkgname="keras"
pkgver="2.2.0"
pkgrel="1"
pkgdesc="Deep Learning library (convnets, recurrent neural networks, and more)"
arch=('any')
url="https://github.com/fchollet/keras"
license=('MIT')
makedepends=('python'  'python-setuptools'  'python-numpy'  'python-scipy'  'python-h5py'  'python-yaml'
             'python2' 'python2-setuptools' 'python2-numpy' 'python2-scipy' 'python2-h5py' 'python2-yaml'
            )
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/fchollet/${_pkgname}/archive/${pkgver}.tar.gz")
sha256sums=('83eae0c251c5ec7e9134e6e79d81da58bfce88e6932fef69dd57c0d512d548f4')

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
  optdepends=('python2-theano' 'cudnn')
  cd "$srcdir/${_pkgname}-${pkgver}-py2"
  python2 setup.py install --root="$pkgdir"/ --optimize=1
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE.txt"
}

package_python-keras() {
  depends=('python' 'python-numpy' 'python-scipy' 'python-h5py' 'python-yaml')
  optdepends=('python-theano' 'python-tensorflow' 'cudnn')
  cd "$srcdir/${_pkgname}-${pkgver}"
  python setup.py install --root="$pkgdir"/ --optimize=1
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE.txt"
}

# vim:set ts=2 sw=2 et:
