# Maintainer: Jingbei Li <i@jingbei.li>
# Contributor: Francois Boulogne <fboulogne at april dot org>
# Contributor: Gaël Donval <gdonval+aur at google mail>
pkgbase='python-toolz'
pkgname=('python-toolz' 'python2-toolz')
_pkgname=toolz
pkgver=0.10.0
pkgrel=1
pkgdesc="A set of utility functions for iterators, functions, and dictionaries."
arch=('any')
url="https://github.com/pytoolz/toolz"
license=('BSD')
makedepends=('python-setuptools' 'python2-setuptools')
source=("$url/archive/${pkgver}.tar.gz")
sha256sums=('48317c9b6bacb7ddde16fb7aa793a6db04cffbdb04733271af2d8904465ed073')

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

package_python2-toolz() {
  depends=('python2')
  cd "$srcdir/${_pkgname}-${pkgver}-py2"
  python2 setup.py install --prefix=/usr --root="$pkgdir" --optimize=1
  install -Dm644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

package_python-toolz() {
  depends=('python')
  cd "$srcdir/${_pkgname}-${pkgver}"
  python setup.py install --prefix=/usr --root="$pkgdir" --optimize=1
  install -Dm644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

# vim:ts=2:sw=2:et:
