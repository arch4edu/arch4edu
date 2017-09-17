# Maintainer: Francois Boulogne <fboulogne at april dot org>
# Contributor: Jingbei Li <i@jingbei.li>
pkgbase=python2-pywavelets
#pkgname=(python-pywavelets python2-pywavelets)
pkgname=python2-pywavelets
_pkgname=pywt
pkgver=0.5.2
pkgrel=1
pkgdesc="Discrete Wavelet Transforms in Python"
arch=('x86_64' 'i686')
url="https://github.com/PyWavelets/pywt"
license=('MIT')
makedepends=('python-setuptools' 'python2-setuptools' 'cython' 'cython2' 'python-numpy' 'python2-numpy')
source=("https://github.com/PyWavelets/pywt/archive/v$pkgver.tar.gz")
sha256sums=('e36d629f40f7781da2dcaa2139bc476e9deaf91d79f675b5ce0bde6e775d1b53')

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
  cd "$srcdir/$_pkgname-$pkgver"
  python setup.py build
}

package_python2-pywavelets(){
  depends=('python2' 'python2-numpy')
  cd "$srcdir/$_pkgname-$pkgver-py2"
  python2 setup.py install --root="$pkgdir/" --optimize=1
  install -Dm644 COPYING "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

package_python-pywavelets(){
  depends=('python' 'python-numpy')
  cd "$srcdir/$_pkgname-$pkgver"
  python setup.py install --root="$pkgdir/" --optimize=1
  install -Dm644 COPYING "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

# vim:ts=2:sw=2:et:
