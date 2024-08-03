# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: David McInnis <dave@dave3.xyz>
# Contributor: Jean Lucas <jean@4ray.co>
# Contributor: McNoggins <gagnon88 at Gmail dot com>
_base=imread
pkgname=python-${_base}
pkgdesc="Read images to numpy arrays"
pkgver=0.7.6
pkgrel=1
arch=(x86_64)
url="https://github.com/luispedro/${_base}"
license=(MIT)
depends=(python-numpy)
makedepends=(python-build python-installer python-setuptools python-wheel libpng libjpeg-turbo libtiff libwebp xcftools)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('7c51d891b28bf907c81c6ce0d69930fa4c090f0472f5ed001497e68c5ff3227d21e2e9b4f88f429082e64b7cf14600c14c4e20370ce39c0e855b2f8c50c2ef2b')

build() {
  cd ${_base}-${pkgver}
  python -m build --wheel --skip-dependency-check --no-isolation
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm 644 COPYING.MIT -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
