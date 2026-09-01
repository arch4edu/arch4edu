# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=charset_normalizer
pkgname=pypy3-${_base/_/-}
pkgdesc="The Real First Universal Charset Detector"
pkgver=3.5.1
pkgrel=1
arch=(any)
url="https://github.com/jawah/${_base}"
license=(MIT)
depends=(pypy3)
makedepends=(pypy3-build pypy3-installer pypy3-setuptools-scm)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz)
sha512sums=('4f3b5bd701c541af34522a507b11798efdcc631ae54508c2ba100258f170bcfc5582ee52b06f75b8977168351e37626269ead866fb3d222af0fe566ed0af8c2a')

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
