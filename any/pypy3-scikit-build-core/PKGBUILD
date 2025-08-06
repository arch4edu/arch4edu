# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=scikit-build-core
pkgname=pypy3-${_base}
pkgdesc="Build backend for CMake based projects"
pkgver=0.11.5
pkgrel=1
arch=(any)
url="https://github.com/${_base/-core/}/${_base}"
license=(Apache-2.0)
depends=(cmake ninja pypy3-packaging pypy3-pathspec)
makedepends=(pypy3-build pypy3-installer pypy3-hatch-vcs)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('f48e9fdd817a07ac6cc3eb38a36be31f7696b11b1dd958c62f8626b0412b6d1813d8c7aed386aba1d3ea6424ab5ace96b4684d65c410d87fc7f76a5959be38ff')

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
