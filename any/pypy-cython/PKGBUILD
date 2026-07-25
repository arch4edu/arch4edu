# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Wu Junyu <wu.junyu.aur@outlook.com>
# Contributor: Michel Zou <xantares09@hotmail.com>
# Contributor: Emmanuel Gil Peyrot <linkmauve@linkmauve.fr
# Contributor: Marti Raudsepp <marti@juffo.org>
_base=cython
pkgbase=pypy-${_base}
pkgname=pypy3-cython
pkgver=3.2.9
pkgrel=1
pkgdesc="C-Extensions for PyPy"
arch=(i686 x86_64)
url="https://${_base}.org"
license=(Apache-2.0)
makedepends=(pypy3-setuptools)
source=(https://pypi.org/packages/source/${_base::1}/${_base}/${_base}-${pkgver}.tar.gz)
sha512sums=('5592d4eca3c522628082a695c514627e12b933cb761be77c97da9dda0dafdc44b16ea6ceb18a773ac32173c96e6150d06fa1d61b99d8f85d0fdc367e105b6bb1')

package_pypy3-cython() {
  depends=(pypy3)

  cd "${srcdir}"/${_base}-${pkgver}
  pypy3 setup.py install --prefix=/opt/pypy3 --root="${pkgdir}" --optimize=1
  sed -i 's|#!.*python|#!/usr/bin/pypy3|' "${pkgdir}"/opt/pypy3/bin/*
}
