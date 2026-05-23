# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Jingbei Li <i@jingbei.li>
_base=build
pkgname=pypy3-${_base}
pkgver=1.5.0
pkgrel=1
pkgdesc="A simple, correct PEP 517 build frontend"
arch=(any)
url="https://${_base}.pypa.io"
license=(MIT)
depends=(pypy3-packaging pypy3-pyproject-hooks)
makedepends=(pypy3-installer pypy3-flit-core)
source=(${_base}-${pkgver}.tar.gz::https://github.com/pypa/${_base}/archive/${pkgver}.tar.gz)
sha512sums=('25f69c82047698e802feaf162a1ee334d32f83689ace3e2116d2329a10310b3bcfc6f2e42242d875f4781dffb364c95112819eb2bdaaecc0ebd4b9c00a94b99b')

build() {
  cd ${_base}-${pkgver}
  pypy3 -m flit_core.wheel
}

package() {
  cd ${_base}-${pkgver}
  pypy3 -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
