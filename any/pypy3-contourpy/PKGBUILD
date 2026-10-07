# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=contourpy
pkgname=pypy3-${_base}
pkgdesc=" Python library for calculating contours in 2D quadrilateral grids"
pkgver=1.4.0
pkgrel=1
arch=(any)
url="https://github.com/${_base}/${_base}"
license=(BSD-3-Clause)
depends=(pypy3)
makedepends=(pypy3-build pypy3-installer pypy3-pybind11 meson-pypy3)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('e48dcc49b452d6ec2a0805938fadb0a1a778ddd3f4909c5e81b2f378fbdfd67d08bff03e8441a57a74dfe8f5c2aaec5e4efa1bccf368eb0d3094adb4a152ac98')

build() {
  cd ${_base}-${pkgver}
  PKG_CONFIG_PATH=$(/opt/pypy3/bin/pybind11-config --pkgconfigdir) \
    pypy3 -m build --wheel --skip-dependency-check --no-isolation
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" pypy3 -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
