# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=pathspec
pkgname=pypy3-${_base}
pkgdesc="Utility library for gitignore style pattern matching of file paths"
pkgver=0.12.1
pkgrel=1
arch=(any)
url="https://github.com/cpburnz/python-${_base}"
license=(MPL2)
depends=(pypy3)
makedepends=(pypy3-build pypy3-installer pypy3-flit-core)
source=(python-${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('ea43cfde362165bc2a7467fd3ecdd9c77385201e7405caeec4c5eadbb5fe80a9452f0b243269e868d1cc84446c18c98daa98fa1ce11e3ec8b72cb09906edce69')

build() {
  cd python-${_base}-${pkgver}
  pypy3 -m build --wheel --skip-dependency-check --no-isolation
}

package() {
  cd python-${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" pypy3 -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
