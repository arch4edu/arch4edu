# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: David McInnis <dave@dave3.xyz>
# Contributor: Jean Lucas <jean@4ray.co>
# Contributor: McNoggins <gagnon88 at Gmail dot com>
_base=imread
pkgname=python-${_base}
pkgdesc="Read images to numpy arrays"
pkgver=0.7.5
pkgrel=1
arch=(x86_64)
url="https://github.com/luispedro/${_base}"
license=(MIT)
depends=(python-numpy)
makedepends=(python-build python-installer python-setuptools python-wheel libpng libjpeg-turbo libtiff libwebp xcftools)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('c03fb3b26ebb29c7a72592896dd6c85d75d658db3c2b29e253bf0612128cbf768d6d0e92397b0174c3f49f75354c99bbb0629bdd7d3b7053d8192f1c9579d691')

build() {
  cd ${_base}-${pkgver}
  python -m build --wheel --skip-dependency-check --no-isolation
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm 644 COPYING.MIT -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
