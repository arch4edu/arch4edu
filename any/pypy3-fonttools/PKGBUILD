# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=fonttools
pkgname=pypy3-${_base}
pkgdesc="Tools to manipulate font files"
pkgver=4.58.2
pkgrel=1
arch=(any)
url="https://github.com/${_base}/${_base}"
license=(MIT)
depends=(pypy3)
makedepends=(pypy3-build pypy3-installer pypy3-setuptools pypy3-cython)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz)
sha512sums=('f78026457be3d75be89ec6788309fc5cab9d9987b5c438bffe7059a78b5d688b6fb9a94dca9636f4c28d44a60f36cdd24bbdf1d32197d63e79b99f3108ce32a5')

build() {
  cd ${_base}-${pkgver}
  pypy3 -m build --wheel --skip-dependency-check --no-isolation
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" pypy3 -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm 644 LICENSE* -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
