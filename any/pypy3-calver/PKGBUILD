# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=calver
pkgname=pypy3-${_base}
pkgdesc="Setuptools extension for CalVer package versions"
pkgver=2025.10.20
pkgrel=1
arch=(any)
url="https://github.com/di/${_base}"
license=(Apache-2.0)
depends=(pypy3)
makedepends=(pypy3-build pypy3-installer pypy3-setuptools)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz)
sha512sums=('248add922c0dbbb13928dd5568494715a515fe0815057115751d668c77f55aa7e0a258018ac2c2af853b363a0d0ea59652f636f6f72f8665d0ca6ac036311ba3')

build() {
  cd ${_base}-${pkgver}
  pypy3 -m build --wheel --skip-dependency-check --no-isolation
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" pypy3 -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
