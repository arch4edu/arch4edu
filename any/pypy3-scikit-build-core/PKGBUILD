# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=scikit-build-core
pkgname=pypy3-${_base}
pkgdesc="Build backend for CMake based projects"
pkgver=0.12.1
pkgrel=1
arch=(any)
url="https://github.com/${_base/-core/}/${_base}"
license=(Apache-2.0)
depends=(cmake ninja pypy3-packaging pypy3-pathspec)
makedepends=(pypy3-build pypy3-installer pypy3-hatch-vcs)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('0a700371fac7c9b689a5d57a8385f17baff2b28f93a1f8448ffb92b127a89dda7ecd4aec642fbfe6b8e38d68b6ca35b45bbfaaee141872abceba72d6a67f85cc')

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
