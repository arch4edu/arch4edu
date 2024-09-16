# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Wu Junyu <wu.junyu.aur@outlook.com>
# Contributor: Daniel Milde <daniel@milde.cz>
# Contributor: Yen Chi Hsuan <yan12125@gmail.com>
_base=setuptools
pkgbase=pypy-${_base}
pkgname=pypy3-${_base}
pkgver=75.0.0
pkgrel=1
epoch=1
pkgdesc="Easily download, build, install, upgrade, and uninstall Python packages"
arch=(any)
url="https://${_base}.pypa.io"
license=(MIT)
makedepends=(pypy3)
source=(https://pypi.org/packages/source/${_base::1}/${_base}/${_base}-${pkgver}.tar.gz)
sha512sums=('78955967c23450822a154db99f9a4cb5d45bfb2fe42797ea39c784e23004172d75fbbba6a6b89fa8c0d63c6b9ffb45e791e48b3d8201cfffc84bd75769cd02ef')

prepare() {
  cd "${srcdir}"/${_base}-${pkgver}
  sed -i -e "s|^#\!.*/usr/bin/env python|#!/usr/bin/env pypy|" setup.py
}

# Rename the following function to check() to enable checking
_check_pypy3-setuptools() {
  # Workaround UTF-8 tests by setting LC_CTYPE

  # Check pypy3 module
  cd "${srcdir}"/${_base}-${pkgver}
  LC_CTYPE=en_US.utf8 pypy3 setup.py ptr
}

package_pypy3-setuptools() {
  depends=(pypy3)
  cd "${srcdir}/${_base}-${pkgver}"
  pypy3 setup.py install --prefix=/opt/pypy3 --root="${pkgdir}" --optimize=1
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
