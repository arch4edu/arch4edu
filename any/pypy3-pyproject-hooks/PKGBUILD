# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=pyproject-hooks
pkgname=pypy3-${_base}
pkgver=1.3.3
pkgrel=1
pkgdesc="A low-level library for calling build-backends in pyproject.toml-based project"
arch=(any)
url="https://github.com/pypa/${_base}"
license=(MIT)
depends=(pypy3)
makedepends=(pypy3-installer pypy3-flit-core)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('866d7c9092202adddc3a6f19856fb34191daf0455bc1abf8bdbabb32d1fc386daa5eaf3a3c5124c5000e2b0b0c70cf51b97c9a02a31c853a7f0bf4ebed2eb1ea')

build() {
  cd ${_base}-${pkgver}
  pypy3 -m flit_core.wheel
}

package() {
  cd ${_base}-${pkgver}
  pypy3 -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
