# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=urllib3
pkgname=pypy3-${_base}
pkgdesc="HTTP library with thread-safe connection pooling, file post, and more"
pkgver=2.4.0
pkgrel=1
arch=(any)
url="https://github.com/${_base}/${_base}"
license=(MIT)
depends=(pypy3)
makedepends=(pypy3-build pypy3-installer pypy3-hatch-vcs)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz)
sha512sums=('78afd6daea5594381783cae2cc3efbfcc89455da7f86994a17bd86c3c840d2e304fd3b744e8c0789cbbe6704502ef03a1bbaaadd2b1713b084adb250cfdffb9f')

build() {
  cd ${_base}-${pkgver}
  export SETUPTOOLS_SCM_PRETEND_VERSION=${pkgver}
  pypy3 -m build --wheel --skip-dependency-check --no-isolation
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" pypy3 -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm 644 LICENSE.txt -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
