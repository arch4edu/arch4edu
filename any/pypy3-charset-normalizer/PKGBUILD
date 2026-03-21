# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=charset_normalizer
pkgname=pypy3-${_base/_/-}
pkgdesc="The Real First Universal Charset Detector"
pkgver=3.4.6
pkgrel=1
arch=(any)
url="https://github.com/jawah/${_base}"
license=(MIT)
depends=(pypy3)
makedepends=(pypy3-build pypy3-installer pypy3-setuptools-scm)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz)
sha512sums=('df4cb1762dc4b40f089c98b7608922d8b0b915d0a59b03ac65971dc5f7c44635ee1de7e081ab5d18157d777b55894006965fe449dbae8adf5a91ea6f00457695')

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
