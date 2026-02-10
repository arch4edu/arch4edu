# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Wu Junyu <wu.junyu.aur@outlook.com>
# Contributor: Daniel Milde <daniel@milde.cz>
# Contributor: Yen Chi Hsuan <yan12125@gmail.com>
_base=setuptools
pkgname=pypy3-${_base}
pkgver=82.0.0
pkgrel=1
epoch=1
pkgdesc="Easily download, build, install, upgrade, and uninstall Python packages"
arch=(any)
url="https://${_base}.pypa.io"
license=(MIT)
makedepends=(pypy3)
source=(https://pypi.org/packages/source/${_base::1}/${_base}/${_base}-${pkgver}.tar.gz)
sha512sums=('52424f813bb8efa1d3aa8cb910338d29c36c6a641f7ded91d298c1abe7c1a24d572c60c14c028f3825af29b46d57a4ee454845b1d22b73b03278a9500d957dd9')

prepare() {
  cd "${srcdir}"/${_base}-${pkgver}
  sed -i -e "s|^#\!.*/usr/bin/env python|#!/usr/bin/env pypy|" setup.py
}

# Rename the following function to check() to enable checking
_check() {
  # Workaround UTF-8 tests by setting LC_CTYPE

  # Check pypy3 module
  cd "${srcdir}"/${_base}-${pkgver}
  LC_CTYPE=en_US.utf8 pypy3 setup.py ptr
}

package() {
  depends=(pypy3)
  cd "${srcdir}/${_base}-${pkgver}"
  pypy3 setup.py install --prefix=/opt/pypy3 --root="${pkgdir}" --optimize=1
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
