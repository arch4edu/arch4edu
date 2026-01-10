# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=pathspec
pkgname=pypy3-${_base}
pkgdesc="Utility library for gitignore style pattern matching of file paths"
pkgver=1.0.3
pkgrel=1
arch=(any)
url="https://github.com/cpburnz/python-${_base}"
license=(MPL2)
depends=(pypy3)
makedepends=(pypy3-build pypy3-installer pypy3-flit-core)
source=(python-${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('daf461339da0b25ed37a5f788e5cdedb4b061249e71ba0c4abbe533a121337e0ed99b7217633b26ab319fb0b6bad2f7a34297d657f7febfdf8efb14b3448076d')

build() {
  cd python-${_base}-${pkgver}
  pypy3 -m build --wheel --skip-dependency-check --no-isolation
}

package() {
  cd python-${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" pypy3 -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
