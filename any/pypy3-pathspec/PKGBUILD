# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=pathspec
pkgname=pypy3-${_base}
pkgdesc="Utility library for gitignore style pattern matching of file paths"
pkgver=1.1.1
pkgrel=1
arch=(any)
url="https://github.com/cpburnz/python-${_base}"
license=(MPL2)
depends=(pypy3)
makedepends=(pypy3-build pypy3-installer pypy3-flit-core)
source=(python-${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('c73f181c3da185952fc061e9245e351ea3162794fd533466a05aab13bb84ef7f863d64df817fc260f7994c5ebe8eec08ebaddbea428b0d90cdd854f976682dc5')

build() {
  cd python-${_base}-${pkgver}
  pypy3 -m build --wheel --skip-dependency-check --no-isolation
}

package() {
  cd python-${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" pypy3 -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
