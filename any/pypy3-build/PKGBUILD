# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Jingbei Li <i@jingbei.li>
_base=build
pkgname=pypy3-${_base}
pkgver=1.4.1
pkgrel=1
pkgdesc="A simple, correct PEP 517 build frontend"
arch=(any)
url="https://${_base}.pypa.io"
license=(MIT)
depends=(pypy3-packaging pypy3-pyproject-hooks)
makedepends=(pypy3-installer pypy3-flit-core)
source=(${_base}-${pkgver}.tar.gz::https://github.com/pypa/${_base}/archive/${pkgver}.tar.gz)
sha512sums=('ed6e6329ee07c547a8cd7568d4f769b50e117a684c1d087380f896183db4bd6c4d921d75913525b301f994ff865d5acbe44290d8a1aa7c13c169979b942ceedc')

build() {
  cd ${_base}-${pkgver}
  pypy3 -m flit_core.wheel
}

package() {
  cd ${_base}-${pkgver}
  pypy3 -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
