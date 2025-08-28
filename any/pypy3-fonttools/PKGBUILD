# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=fonttools
pkgname=pypy3-${_base}
pkgdesc="Tools to manipulate font files"
pkgver=4.59.2
pkgrel=1
arch=(any)
url="https://github.com/${_base}/${_base}"
license=(MIT)
depends=(pypy3)
makedepends=(pypy3-build pypy3-installer pypy3-setuptools pypy3-cython)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz)
sha512sums=('34a36048680e2494f49a0fd5b94352face4cd5727e8748cbfccb6ec71f44d69d155bba43de7b9244d91723c762101216f4b057e4f64a577197f79c1db269eaff')

build() {
  cd ${_base}-${pkgver}
  pypy3 -m build --wheel --skip-dependency-check --no-isolation
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" pypy3 -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm 644 LICENSE* -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
