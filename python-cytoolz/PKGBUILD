# Maintainer: Jingbei Li <i@jingbei.li>
# Contributor: Francois Boulogne <fboulogne at april dot org>
# Contributor: Gaël Donval <gdonval+aur at google mail>
pkgbase='python-cytoolz'
pkgname=('python-cytoolz' 'python2-cytoolz')
_pkgname=cytoolz
pkgver=0.9.0
pkgrel=5
pkgdesc="Cython implementation of the toolz package, which provides high performance utility functions for iterables, functions, and dictionaries."
arch=('x86_64')
url="https://github.com/pytoolz/cytoolz"
license=('BSD')
makedepends=('cython' 'cython2' 'python-setuptools' 'python2-setuptools')
source=("$url/archive/${pkgver}.tar.gz")
sha256sums=('177d6bcf76d60efeb5fa04c151e8c2e53a2679d380f1d316b0fd3a1cdffd75fb')

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

package_python2-cytoolz() {
  depends=('python2')
  provides=('python2-toolz')
  conflicts=('python2-toolz')
  cd "$srcdir/${_pkgname}-${pkgver}-py2"
  python2 setup.py install --prefix=/usr --root="$pkgdir" --optimize=1
  install -Dm644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

package_python-cytoolz() {
  depends=('python')
  provides=('python-toolz')
  conflicts=('python-toolz')
  cd "$srcdir/${_pkgname}-${pkgver}"
  python setup.py install --prefix=/usr --root="$pkgdir" --optimize=1
  install -Dm644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

# vim:ts=2:sw=2:et:
