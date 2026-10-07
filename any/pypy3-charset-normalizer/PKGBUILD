# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=charset_normalizer
pkgname=pypy3-${_base/_/-}
pkgdesc="The Real First Universal Charset Detector"
pkgver=3.5.2
pkgrel=1
arch=(any)
url="https://github.com/jawah/${_base}"
license=(MIT)
depends=(pypy3)
makedepends=(pypy3-build pypy3-installer pypy3-setuptools-scm)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz)
sha512sums=('cbcb39e42261bacc9e5a2554e361cd5481061090d6eda1ac355b9fcf95c1793e7cb771738704e9b947812466b67a75721c5a3586b7d8ec8604ea2d27c5b6bcbc')

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
