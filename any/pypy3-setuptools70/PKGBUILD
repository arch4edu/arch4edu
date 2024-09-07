# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=setuptools
pkgname=pypy3-${_base}70
pkgver=70.3.0
pkgrel=1
epoch=1
pkgdesc="Easily download, build, install, upgrade, and uninstall Python packages"
arch=(any)
url="https://${_base}.pypa.io"
license=(MIT)
depends=(pypy3)
provides=(pypy3-${base}=${pkgver})
conflicts=(pypy3-${base})
source=(https://pypi.org/packages/source/${_base::1}/${_base}/${_base}-${pkgver}.tar.gz)
sha512sums=('9f330bd9867631da69ee0886551033a6e8ef3cf52cfe38aad9fcd359cbfc2e0d7ee8c85382b29f8d52568c674893dc07f2b2a896afe5154e6140bb3209ee50a0')

prepare() {
  cd ${_base}-${pkgver}
  sed -i -e "s|^#\!.*/usr/bin/env python|#!/usr/bin/env pypy|" setup.py
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" pypy3 setup.py install --prefix=/opt/pypy3 --root="${pkgdir}" --optimize=1
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
