# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=scikit-build-core
pkgname=pypy3-${_base}
pkgdesc="Build backend for CMake based projects"
pkgver=0.12.2
pkgrel=1
arch=(any)
url="https://github.com/${_base/-core/}/${_base}"
license=(Apache-2.0)
depends=(cmake ninja pypy3-packaging pypy3-pathspec)
makedepends=(pypy3-build pypy3-installer pypy3-hatch-vcs)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('02e0f92684b5f3678f64565e09c896748cbb5b8e03e004abfd108a6c435731cd49b23952566f215ca77813dfb8429cdb5aea7a1fcf5b8edc40fc60a14e7ec31c')

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
