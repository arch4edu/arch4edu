# Maintainer: Oliver Harley <oliver.r.harley+aur@gmail.com>
_pkgname=keras-applications
pkgbase=python-keras-applications
pkgname=("python-keras-applications" "python2-keras-applications")
pkgver=1.0.4
pkgrel=1
# Needs git as a makedep
#pkgver() {
#   git ls-remote $url | sort -Vr | \
#   grep -o --regexp 'refs/tags/[0-9]\{1,\}.[0-9]\{1,\}.[0-9]\{1,\}$' | \
#   grep -o --regexp           '[0-9]\{1,\}.[0-9]\{1,\}.[0-9]\{1,\}$' | head -n 1
#}
pkgdesc="Applications module of the Keras deep learning library"
arch=('any')
url="https://github.com/keras-team/keras-applications/"
license=('MIT')
provides=(python-keras-applications)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/keras-team/${_pkgname}/archive/${pkgver}.tar.gz")
sha256sums=('37bd2f3ba9c0e0105c193999b1162fd99562cf43e5ef06c73932950ecc46d085')
makedepends=('python' 'python-setuptools' 'python-numpy'    'python-keras'
             'python2' 'python2-setuptools' 'python2-numpy' #'python2-keras' # uncomment for py2
             )

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

package_python2-keras-applications() {
  depends=('python2' 'python2-numpy' 'python2-keras')
  #optdepends=('python2-theano' 'cudnn')
  cd "$srcdir/${_pkgname}-${pkgver}-py2"
  python2 setup.py install --root="${pkgdir}"/ --optimize=1
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE.txt"
}

package_python-keras-applications() {
  depends=('python' 'python-numpy' 'python-keras')
  cd "$srcdir/${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}"/ --optimize=1
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE.txt"
}

