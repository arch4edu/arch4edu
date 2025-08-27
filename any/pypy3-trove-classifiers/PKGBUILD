# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=trove-classifiers
pkgname=pypy3-${_base}
pkgdesc="Canonical source for classifiers on PyPI"
pkgver=2025.8.26.11
pkgrel=1
arch=(any)
url="https://github.com/pypa/${_base}"
license=(Apache-2.0)
depends=(pypy3)
makedepends=(pypy3-build pypy3-installer pypy3-setuptools pypy3-calver)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz)
sha512sums=('61d59c8943f95fb74f0817fbb7f42a40b9fdf775ab9991e8d5af4ddd2a1450da6d11a96531b32726f677470f71e94c28736b54385fdd670661a0297bc76b04ec')

build() {
  cd ${_base}-${pkgver}
  pypy3 -m build --wheel --skip-dependency-check --no-isolation
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" pypy3 -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
