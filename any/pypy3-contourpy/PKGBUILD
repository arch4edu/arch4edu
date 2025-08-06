# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=contourpy
pkgname=pypy3-${_base}
pkgdesc=" Python library for calculating contours in 2D quadrilateral grids"
pkgver=1.3.3
pkgrel=1
arch=(any)
url="https://github.com/${_base}/${_base}"
license=(BSD-3-Clause)
depends=(pypy3)
makedepends=(pypy3-build pypy3-installer pypy3-pybind11 meson-pypy3)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('b920fc30189075cb29d6af346d0b7c9038b46b03c561388652eaf0d9647cb5246894903742c230b99fe5e3e62c6a60fcb634a24c31da6930819acd2eefb5f631')

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
