# Maintainer: Jingbei Li <i@jingbei.li>
pkgbase=python-glob2
pkgname=python-glob2
#pkgname=(python-glob2 python2-glob2)
pkgver=0.6
pkgrel=1
pkgdesc="An extended version of Python's builtin glob module that can capture patterns and supports recursive wildcards."
arch=('any')
url="https://github.com/miracle2k/python-glob2"
license=('custom')
makedepends=('git' 'python-setuptools' 'python2-setuptools')
source=("git+$url#tag=${pkgver}")
md5sums=('SKIP')

prepare() {
  cd "$srcdir/"
  cp -a "${pkgbase}" "${pkgbase}-py2"
  cd "${pkgbase}-py2"
  sed -e "s|#![ ]*/usr/bin/python$|#!/usr/bin/python2|" \
    -e "s|#![ ]*/usr/bin/env python$|#!/usr/bin/env python2|" \
    -e "s|#![ ]*/bin/env python$|#!/usr/bin/env python2|" \
    -i $(find . -name '*.py')
}

build() {
  msg2 "Building Python 2"
  cd "$srcdir/${pkgbase}-py2"
  python2 setup.py build

  msg2 "Building Python 3"
  cd "$srcdir/${pkgbase}"
  python setup.py build
}

package_python2-glob2() {
  depends=('python2')
  cd "$srcdir/${pkgbase}-py2"
  python2 setup.py install --root="$pkgdir"/ --optimize=1
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

package_python-glob2() {
  depends=('python')
  cd "$srcdir/${pkgbase}"
  python setup.py install --root="$pkgdir"/ --optimize=1
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

# vim:set ts=2 sw=2 et:
