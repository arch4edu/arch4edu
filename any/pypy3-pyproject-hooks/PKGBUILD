# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=pyproject-hooks
pkgname=pypy3-${_base}
pkgver=1.2.0
pkgrel=1
pkgdesc="A low-level library for calling build-backends in pyproject.toml-based project"
arch=(any)
url="https://github.com/pypa/${_base}"
license=(MIT)
depends=(pypy3)
makedepends=(pypy3-installer pypy3-flit-core)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('c198624ca278001922e07039333aa623a87bd9ef9f38ec98346d6d49f19dec422f788f6737623b461d76586bc8fa752518906bc7501e822429803881700ce701')

build() {
  cd ${_base}-${pkgver}
  pypy3 -m flit_core.wheel
}

package() {
  cd ${_base}-${pkgver}
  pypy3 -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
