# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=trove-classifiers
pkgname=pypy3-${_base}
pkgdesc="Canonical source for classifiers on PyPI"
pkgver=2025.9.11.17
pkgrel=1
arch=(any)
url="https://github.com/pypa/${_base}"
license=(Apache-2.0)
depends=(pypy3)
makedepends=(pypy3-build pypy3-installer pypy3-setuptools pypy3-calver)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz)
sha512sums=('178f74c8df24395edf08beba74e830ee45a9644a18d2b3910e863468d67cca9fee97a11bdbbebf927afdada5a3188a510ef7f9ac7dba2095e839b05b573d2d03')

build() {
  cd ${_base}-${pkgver}
  pypy3 -m build --wheel --skip-dependency-check --no-isolation
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" pypy3 -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
