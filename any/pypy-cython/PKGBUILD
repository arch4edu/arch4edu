# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Wu Junyu <wu.junyu.aur@outlook.com>
# Contributor: Michel Zou <xantares09@hotmail.com>
# Contributor: Emmanuel Gil Peyrot <linkmauve@linkmauve.fr
# Contributor: Marti Raudsepp <marti@juffo.org>
_base=cython
pkgbase=pypy-${_base}
pkgname=pypy3-cython
pkgver=3.2.1
pkgrel=1
pkgdesc="C-Extensions for PyPy"
arch=(i686 x86_64)
url="https://${_base}.org"
license=(Apache-2.0)
makedepends=(pypy3-setuptools)
source=(https://pypi.org/packages/source/${_base::1}/${_base}/${_base}-${pkgver}.tar.gz)
sha512sums=('b6f64b2c32c355a9c5a3586fdea768ad1924cb4b421d4395d443dadc1cf06e2fe4f3f85d237789eb0a68c9857750cbefefb022475ed7f3d8787551bea3d2fb7d')

package_pypy3-cython() {
  depends=(pypy3)

  cd "${srcdir}"/${_base}-${pkgver}
  pypy3 setup.py install --prefix=/opt/pypy3 --root="${pkgdir}" --optimize=1
  sed -i 's|#!.*python|#!/usr/bin/pypy3|' "${pkgdir}"/opt/pypy3/bin/*
}
