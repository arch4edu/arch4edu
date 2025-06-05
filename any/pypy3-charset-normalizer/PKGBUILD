# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=charset_normalizer
pkgname=pypy3-${_base/_/-}
pkgdesc="The Real First Universal Charset Detector"
pkgver=3.4.2
pkgrel=1
arch=(any)
url="https://github.com/jawah/${_base}"
license=(MIT)
depends=(pypy3)
makedepends=(pypy3-build pypy3-installer pypy3-setuptools-scm)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz)
sha512sums=('5b5197ad615a330d29fdb4ce910af085e19e283e229c6ee96ab19a1ccc0f60dc0863ba8c4818094b993295d39b3f4112c530d493b73e19ef73913e17a91c9e6f')

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
