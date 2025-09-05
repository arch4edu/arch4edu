# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=dateutil
pkgname=pypy3-${_base}
pkgdesc="Extensions to the standard Python datetime module"
pkgver=2.9.0.post0
pkgrel=1
arch=(any)
url="https://github.com/${_base}/${_base}"
license=(Apache-2.0 BSD-3-Clause)
depends=(pypy3)
makedepends=(pypy3-build pypy3-installer pypy3-setuptools-scm)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz)
sha512sums=('8ba2bf0f5a0d74298094c638368ec58033b47b5abd3b3bc182e0fec753e8d5fb8592eb6a6db22a1f7a9d48cf90e414ccbafea25208dcd148a16dd907007f52d0')

build() {
  cd ${_base}-${pkgver}
  export SETUPTOOLS_SCM_PRETEND_VERSION=${pkgver}
  pypy3 -m build --wheel --skip-dependency-check --no-isolation
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" pypy3 -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
