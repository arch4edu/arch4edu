# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=fonttools
pkgname=pypy3-${_base}
pkgdesc="Tools to manipulate font files"
pkgver=4.64.0
pkgrel=1
arch=(any)
url="https://github.com/${_base}/${_base}"
license=(MIT)
depends=(pypy3)
makedepends=(pypy3-build pypy3-installer pypy3-setuptools pypy3-cython)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz)
sha512sums=('1cf3d8ab10931e6eca3f54e2d365a946413d90e2a8fe0405252db14a51e2908c109c6a65f7b0fb5fabaeb0e30eb27b5b737bf2d1b75a3137806bc88f140a0faa')

build() {
  cd ${_base}-${pkgver}
  pypy3 -m build --wheel --skip-dependency-check --no-isolation
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" pypy3 -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm 644 LICENSE* -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
