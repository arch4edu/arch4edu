# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=calver
pkgname=pypy3-${_base}
pkgdesc="Setuptools extension for CalVer package versions"
pkgver=2025.04.17
pkgrel=1
arch=(any)
url="https://github.com/di/${_base}"
license=(Apache-2.0)
depends=(pypy3)
makedepends=(pypy3-build pypy3-installer pypy3-setuptools)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz)
sha512sums=('9d15bfefd02be1d6449beaed4f9dc8b5662442ebb747153cea1ea246c484c9240f449126fef3f175a2e66d49ec75112aaf91cf28f966abf4109d22ef2932e022')

build() {
  cd ${_base}-${pkgver}
  pypy3 -m build --wheel --skip-dependency-check --no-isolation
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" pypy3 -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
