# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=cppy
pkgname=pypy3-${_base}
pkgdesc="A collection of C++ headers which make it easier to write Python C extension modules"
pkgver=1.3.1
pkgrel=1
arch=(any)
url="https://github.com/nucleic/${_base}"
license=(BSD-3-Clause)
depends=(pypy3-setuptools)
makedepends=(pypy3-build pypy3-installer pypy3-setuptools-scm)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz)
sha512sums=('5f2b9bbb500385dd138aa6eb4eb37c495f36b550554ef8f26c88802a69f5b5118549e010fdb2e526c19a0de1fc988642d7cdec6f357a1cd87edc3bf9a74fcfc9')

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
