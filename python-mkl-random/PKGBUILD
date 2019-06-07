# Maintainer: Jingbei Li <i@jingbei.li>
pkgbase=python-mkl-random
pkgname=(python-mkl-random python2-mkl-random)
_pkgname=mkl_random
pkgver=1.0.4
pkgrel=2
pkgdesc="NumPy-based Python interface to Intel (R) MKL Random Number Generation functionality"
arch=('x86_64')
url="https://github.com/IntelPython/mkl_random"
license=('custom')
depends=('intel-mkl')
makedepends=('cython' 'cython2' 'git' 'intel-compiler-base' 'python-numpy' 'python2-numpy' 'python-setuptools' 'python2-setuptools')
source=("git+$url#tag=v${pkgver}")
md5sums=('SKIP')

prepare() {
  cd "$srcdir/"
  cp -a "${_pkgname}" "${_pkgname}-py2"
  cd "${_pkgname}-py2"
  sed -e "s|#![ ]*/usr/bin/python$|#!/usr/bin/python2|" \
    -e "s|#![ ]*/usr/bin/env python$|#!/usr/bin/env python2|" \
    -e "s|#![ ]*/bin/env python$|#!/usr/bin/env python2|" \
    -i $(find . -name '*.py')
}

build() {
  msg "Building Python 2"
  cd "$srcdir/${_pkgname}-py2"
  python2 setup.py build

  msg "Building Python 3"
  cd "$srcdir/${_pkgname}"
  python setup.py build
}

package_python2-mkl-random() {
  depends+=('python2-numpy')
  cd "$srcdir/${_pkgname}-py2"
  python2 setup.py install --root="$pkgdir"/ --optimize=1
  install -Dm644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

package_python-mkl-random() {
  depends+=('python-numpy')
  cd "$srcdir/${_pkgname}"
  python setup.py install --root="$pkgdir"/ --optimize=1
  install -Dm644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

# vim:set ts=2 sw=2 et:
