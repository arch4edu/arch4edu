# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Wu Junyu <wu.junyu.aur@outlook.com>
# Contributor: Michel Zou <xantares09@hotmail.com>
# Contributor: Emmanuel Gil Peyrot <linkmauve@linkmauve.fr
# Contributor: Marti Raudsepp <marti@juffo.org>
_base=cython
pkgbase=pypy-${_base}
pkgname=pypy3-cython
pkgver=3.2.3
pkgrel=1
pkgdesc="C-Extensions for PyPy"
arch=(i686 x86_64)
url="https://${_base}.org"
license=(Apache-2.0)
makedepends=(pypy3-setuptools)
source=(https://pypi.org/packages/source/${_base::1}/${_base}/${_base}-${pkgver}.tar.gz)
sha512sums=('00bf2244da9c544fd3ea110cd1ab2aeadeb7e1df16fff4fdc926b90759c75f312c11171513d55dad6b5489f77c7c462905b789242641d6d6807b172db1a57b87')

package_pypy3-cython() {
  depends=(pypy3)

  cd "${srcdir}"/${_base}-${pkgver}
  pypy3 setup.py install --prefix=/opt/pypy3 --root="${pkgdir}" --optimize=1
  sed -i 's|#!.*python|#!/usr/bin/pypy3|' "${pkgdir}"/opt/pypy3/bin/*
}
