# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Jingbei Li <i@jingbei.li>
_base=build
pkgname=pypy3-${_base}
pkgver=1.2.2.post1
pkgrel=4
pkgdesc="A simple, correct PEP 517 build frontend"
arch=(any)
url="https://${_base}.pypa.io"
license=(MIT)
depends=(pypy3-packaging pypy3-pyproject-hooks)
makedepends=(pypy3-installer pypy3-flit-core)
source=(${_base}-${pkgver}.tar.gz::https://github.com/pypa/${_base}/archive/${pkgver}.tar.gz)
sha512sums=('bdf023c6b578ea77c7fc49c71c7d908bcc9ff6b9255b2767e45b09aca0a39a5297d264695a864fe34772e5d8898a18a90f6e262514bf90daf14db762a8bbe4be')

build() {
  cd ${_base}-${pkgver}
  pypy3 -m flit_core.wheel
}

package() {
  cd ${_base}-${pkgver}
  pypy3 -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
