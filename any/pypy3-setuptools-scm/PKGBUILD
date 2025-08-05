# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=setuptools-scm
pkgname=pypy3-${_base}
pkgdesc="the blessed package to manage your versions by scm tags"
pkgver=9.0.0
pkgrel=1
arch=(any)
url="https://github.com/pypa/${_base}"
license=(MIT)
depends=(pypy3-packaging pypy3-setuptools)
makedepends=(pypy3-build pypy3-installer)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('498131e6699a28a5e6031a7492beb5e885d73a72d0799c7e76a1e237ad546cbb4c7dc20a8ace0398540e02d8a48a8e3fcc78874626b0ce438436f0218ca55346')

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
