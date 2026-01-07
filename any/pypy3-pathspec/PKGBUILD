# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=pathspec
pkgname=pypy3-${_base}
pkgdesc="Utility library for gitignore style pattern matching of file paths"
pkgver=1.0.1
pkgrel=1
arch=(any)
url="https://github.com/cpburnz/python-${_base}"
license=(MPL2)
depends=(pypy3)
makedepends=(pypy3-build pypy3-installer pypy3-flit-core)
source=(python-${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('5fc943fe6336b5b7b2c623bff91d952aa9096bd8b9d90e8cefd9ab189874826f821eefc3d9c97d75fdcb25d73ecff0cd023af613ed4af04a8efe102408346f4f')

build() {
  cd python-${_base}-${pkgver}
  pypy3 -m build --wheel --skip-dependency-check --no-isolation
}

package() {
  cd python-${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" pypy3 -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
