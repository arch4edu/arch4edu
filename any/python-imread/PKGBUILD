# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: David McInnis <dave@dave3.xyz>
# Contributor: Jean Lucas <jean@4ray.co>
# Contributor: McNoggins <gagnon88 at Gmail dot com>
_base=imread
pkgname=python-${_base}
pkgdesc="Read images to numpy arrays"
pkgver=0.7.4
pkgrel=2
arch=(x86_64)
url="https://github.com/luispedro/${_base}"
license=(MIT)
depends=(python-numpy)
makedepends=(python-setuptools libpng libjpeg-turbo libtiff libwebp xcftools)
checkdepends=(python-nose)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('6ec445ede6a25f57f2ab6ab3b4a89b91015edc6a73cb03124c746a21c4fcb1486abb88cf8d9980347afb4ed6b916bfd450b003ded1dc21aa1732c84472a90d28')

build() {
  cd ${_base}-${pkgver}
  python setup.py build
}

check() {
  cd ${_base}-${pkgver}
  python setup.py test
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm 644 COPYING.MIT -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
