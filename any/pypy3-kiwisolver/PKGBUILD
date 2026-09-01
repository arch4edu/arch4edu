# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=kiwi
pkgname=pypy3-${_base}solver
pkgdesc="A fast implementation of the Cassowary constraint solver"
pkgver=1.5.1
pkgrel=1
arch=(any)
url="https://github.com/nucleic/${_base}"
license=(Artistic-1.0-Perl)
depends=(pypy3)
makedepends=(pypy3-build pypy3-installer pypy3-setuptools-scm pypy3-cppy)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz)
sha512sums=('4f1a7107c88adcbd6004d3e28d2f345919d3e0a912036b5406240e42c4b9f34fe2c170c3f4ed9c6286234e2c9cb03ae59a73fb0bc09106cf77bca5cdc267abb2')

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
