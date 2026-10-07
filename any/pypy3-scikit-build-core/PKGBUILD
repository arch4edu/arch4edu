# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=scikit-build-core
pkgname=pypy3-${_base}
pkgdesc="Build backend for CMake based projects"
pkgver=1.1.1
pkgrel=1
arch=(any)
url="https://github.com/${_base/-core/}/${_base}"
license=(Apache-2.0)
depends=(cmake ninja pypy3-packaging pypy3-pathspec)
makedepends=(pypy3-build pypy3-installer pypy3-hatch-vcs)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('6dc9cc2bdc6e621973c73b5de7daebd34bae12e5e45957c39e6de3173c1dd2c2628f1e8ecbc76a7ed2eb4423131ab44ebd7f95741e92d82aacb824dfecb0b597')

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
