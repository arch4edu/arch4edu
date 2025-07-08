# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=contourpy
pkgname=pypy3-${_base}
pkgdesc=" Python library for calculating contours in 2D quadrilateral grids"
pkgver=1.3.2
pkgrel=2
arch=(any)
url="https://github.com/${_base}/${_base}"
license=(BSD-3-Clause)
depends=(pypy3)
makedepends=(pypy3-build pypy3-installer pypy3-pybind11 meson-pypy3)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('4948f1fc706623ec63828066efb0fa720a946e39b3d9072356dea9d27ba07fe5fa37df297a865afd4e96e43419983161e3c7a1fe75d14973460683342bea4f0c')

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
