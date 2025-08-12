# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=kiwi
pkgname=pypy3-${_base}solver
pkgdesc="A fast implementation of the Cassowary constraint solver"
pkgver=1.4.9
pkgrel=1
arch=(any)
url="https://github.com/nucleic/${_base}"
license=(Artistic-1.0-Perl)
depends=(pypy3)
makedepends=(pypy3-build pypy3-installer pypy3-setuptools-scm pypy3-cppy)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz)
sha512sums=('a59db8f06632317cc315dcacfc8884934aa5986b5f75d44631d8de4ed6b264c004fb46f26ffcab2a5f5a9daeb700b727922aa9a28b46657d52863acab5ab2d83')

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
