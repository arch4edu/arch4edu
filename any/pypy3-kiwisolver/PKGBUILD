# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=kiwi
pkgname=pypy3-${_base}solver
pkgdesc="A fast implementation of the Cassowary constraint solver"
pkgver=1.4.8
pkgrel=1
arch=(any)
url="https://github.com/nucleic/${_base}"
license=(Artistic-1.0-Perl)
depends=(pypy3)
makedepends=(pypy3-build pypy3-installer pypy3-setuptools-scm pypy3-cppy)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz)
sha512sums=('487bfd8c59b85b67724da81e2c758e2800b4bf8e76929fc7ea75fe03a3759cc8a57943c8d8940b8d5e75d6e748e236250129bc929303e999a5431f4212b753f2')

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
