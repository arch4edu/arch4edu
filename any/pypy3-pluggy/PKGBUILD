# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=pluggy
pkgname=pypy3-${_base}
pkgdesc="plugin and hook calling mechanisms for python"
pkgver=1.7.0
pkgrel=1
arch=(any)
url="https://github.com/pytest-dev/${_base}"
license=(MIT)
depends=(pypy3)
makedepends=(pypy3-build pypy3-installer pypy3-setuptools-scm)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz)
sha512sums=('ff1b820df39bb6fb037f17178663f54d982f7518bff09e073af06229c549cf39d3bda2c2906b2c8c5f75754e2e4b71864d9a5c454ee3eb6d72d6006b79877099')

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
