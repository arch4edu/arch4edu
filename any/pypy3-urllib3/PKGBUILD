# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=urllib3
pkgname=pypy3-${_base}
pkgdesc="HTTP library with thread-safe connection pooling, file post, and more"
pkgver=2.5.0
pkgrel=1
arch=(any)
url="https://github.com/${_base}/${_base}"
license=(MIT)
depends=(pypy3)
makedepends=(pypy3-build pypy3-installer pypy3-hatch-vcs)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz)
sha512sums=('492ebb3e0481ee5433f45bef184ddb01714dedcbe2eb61665c781f3dcd0d9a226204052d64215c02e8972155560bc146395022723f79c076cb59abe1c0ef51ff')

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
