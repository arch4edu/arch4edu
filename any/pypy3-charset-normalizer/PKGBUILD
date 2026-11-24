# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=charset_normalizer
pkgname=pypy3-${_base/_/-}
pkgdesc="The Real First Universal Charset Detector"
pkgver=3.5.3
pkgrel=1
arch=(any)
url="https://github.com/jawah/${_base}"
license=(MIT)
depends=(pypy3)
makedepends=(pypy3-build pypy3-installer pypy3-setuptools-scm)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz)
sha512sums=('33b52b6c27498c21cfb83c76bf3ac3c80fbcd77c76d4241359f38aea03b337d1c96345164667bd55790a2afb2476bbf8613046eae7a49ef6e7fefa6db2f40459')

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
