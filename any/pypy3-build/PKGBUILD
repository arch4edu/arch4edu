# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=build
pkgname=pypy3-${_base}
pkgver=0.9.0
pkgrel=1
pkgdesc="A simple, correct PEP 517 build frontend"
arch=(any)
url="https://${_base}.pypa.io"
license=(MIT)
makedepends=(pypy3-setuptools)
source=(${_base}-${pkgver}.tar.gz::https://github.com/pypa/${_base}/archive/${pkgver}.tar.gz)
sha512sums=('d6ef229c8f3b348cc939af6bd9a0a521a25c3a5702a95da8ee36d7a1ad3f3e22e10b5c96495ff08a1328ab73f03feebc64e89ce165862cb295eff4360c79d642')

build() {
  cd ${_base}-${pkgver}
  pypy3 setup.py build
}

package() {
  cd ${_base}-${pkgver}
  pypy3 setup.py install --prefix=/opt/pypy3 --root="$pkgdir" --optimize=1 --skip-build
  mkdir -p "$pkgdir/usr"
  mv "${pkgdir}/opt/pypy3/bin" "$pkgdir/usr/bin"
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
