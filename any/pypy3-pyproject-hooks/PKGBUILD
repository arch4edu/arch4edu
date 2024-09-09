# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=pyproject-hooks
pkgname=pypy3-${_base}
pkgver=1.1.0
pkgrel=1
pkgdesc="A low-level library for calling build-backends in pyproject.toml-based project"
arch=(any)
url="https://github.com/pypa/${_base}"
license=(MIT)
depends=(pypy3)
makedepends=(pypy3-build pypy3-installer pypy3-flit-core)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('256028d13adbe35126a63431a2a49e0c48adddce5ffc3ff2eebad368eee7ce52591ecfd8a8526876de20bc59dfc87156533d6a97b55538a739873e60f9509eff')

build() {
  cd ${_base}-${pkgver}
  pypy3 -m build --wheel --skip-dependency-check --no-isolation
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" pypy3 -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
