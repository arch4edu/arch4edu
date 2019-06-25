# Maintainer: Jingbei Li <i@jingbei.li>
# Contributor: Francois Boulogne <fboulogne at april dot org>
# Contributor: Gaël Donval <gdonval+aur at google mail>
pkgbase='python-cytoolz'
pkgname=('python-cytoolz' 'python2-cytoolz')
_pkgname=cytoolz
pkgver=0.9.0.1
pkgrel=5
pkgdesc="Cython implementation of the toolz package, which provides high performance utility functions for iterables, functions, and dictionaries."
arch=('x86_64')
url="https://github.com/pytoolz/cytoolz"
license=('BSD')
makedepends=('cython' 'cython2' 'python-setuptools' 'python2-setuptools')
#source=("$url/archive/${pkgver}.tar.gz")
source=("https://files.pythonhosted.org/packages/36/f4/9728ba01ccb2f55df9a5af029b48ba0aaca1081bbd7823ea2ee223ba7a42/cytoolz-0.9.0.1.tar.gz")
sha256sums=('84cc06fa40aa310f2df79dd440fc5f84c3e20f01f9f7783fc9c38d0a11ba00e5')

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
  cd "$srcdir/${_pkgname}-${pkgver}-py2"
  python2 setup.py install --prefix=/usr --root="$pkgdir" --optimize=1
  install -Dm644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

package_python-cytoolz() {
  depends=('python')
  cd "$srcdir/${_pkgname}-${pkgver}"
  python setup.py install --prefix=/usr --root="$pkgdir" --optimize=1
  install -Dm644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

# vim:ts=2:sw=2:et:
