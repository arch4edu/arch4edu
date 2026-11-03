# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Wu Junyu <wu.junyu.aur@outlook.com>
# Contributor: Michel Zou <xantares09@hotmail.com>
# Contributor: Emmanuel Gil Peyrot <linkmauve@linkmauve.fr
# Contributor: Marti Raudsepp <marti@juffo.org>
_base=cython
pkgbase=pypy-${_base}
pkgname=pypy3-cython
pkgver=3.3.1
pkgrel=1
pkgdesc="C-Extensions for PyPy"
arch=(i686 x86_64)
url="https://${_base}.org"
license=(Apache-2.0)
makedepends=(pypy3-setuptools)
source=(https://pypi.org/packages/source/${_base::1}/${_base}/${_base}-${pkgver}.tar.gz)
sha512sums=('ba12683b6faadd6914c0b87fa5cbfbb37453e3030a0ed8080e128d98f8fba6d49387003f62b4f75f3bb00ee20d04db88f7babcda279af96f24df196c3d1a8e0b')

package_pypy3-cython() {
  depends=(pypy3)

  cd "${srcdir}"/${_base}-${pkgver}
  pypy3 setup.py install --prefix=/opt/pypy3 --root="${pkgdir}" --optimize=1
  sed -i 's|#!.*python|#!/usr/bin/pypy3|' "${pkgdir}"/opt/pypy3/bin/*
}
