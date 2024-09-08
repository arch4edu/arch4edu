# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=flit_core
pkgname=pypy3-${_base//_/-}
pkgver=3.9.0
pkgrel=1
pkgdesc="A PEP 517 build backend for packages using Flit"
arch=(any)
url="https://github.com/pypa/${_base::4}/tree/main/${_base}"
license=(BSD-3-Clause)
depends=(pypy3)
makedepends=(pypy3-build pypy3-installer)
source=(${_base::4}-${pkgver}.tar.gz::https://github.com/pypa/${_base::4}/archive/${pkgver}.tar.gz)
sha512sums=('1218756afcb79af1df0020548102ba29245a9fa998d332357a2a6a2b7b543dda835918f4811ba343e86e1f7c6b45a6dcafe26f8e905c1e49734141f7d4e9f4fc')

build() {
  cd ${_base::4}-${pkgver}/${_base}
  pypy3 -m build --wheel --skip-dependency-check --no-isolation
}

package() {
  cd ${_base::4}-${pkgver}/${_base}
  pypy3 -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
