# Maintainer: Jingbei Li <i@jingbei.li>
# Contributer: Jose Riha <jose1711 gmail com>
pkgbase=python-librosa
pkgname=(python-librosa python2-librosa)
_pkgname=librosa
pkgver=0.6.3
pkgrel=1
pkgdesc="Python library for music and audio analysis"
arch=('any')
url="http://librosa.github.io/librosa"
license=('ISC')
makedepends=('python-setuptools' 'python2-setuptools')
source=("https://github.com/librosa/librosa/archive/${pkgver}.tar.gz")
md5sums=('f77e6d1db202934e4f53699793222009')

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

package_python2-librosa() {
  depends=('python2-joblib' 'python2-matplotlib' 'python2-audioread' 'python2-decorator' 'python2-scikit-learn' 'python2-resampy')
  cd "$srcdir/${_pkgname}-${pkgver}-py2"
  python2 setup.py install --root="$pkgdir"/ --optimize=1
  install -Dm644 LICENSE.md "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

package_python-librosa() {
  depends=('python-joblib' 'python-matplotlib' 'python-audioread' 'python-decorator' 'python-scikit-learn' 'python-resampy')
  cd "$srcdir/${_pkgname}-${pkgver}"
  python setup.py install --root="$pkgdir"/ --optimize=1
  install -Dm644 LICENSE.md "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

# vim:set ts=2 sw=2 et:
