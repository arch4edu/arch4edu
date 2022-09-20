# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=ffcx
pkgname=python-fenics-${_base}
pkgdesc="The FEniCSx Form Compiler"
pkgver=0.5.0.post0
pkgrel=1
arch=(x86_64)
url="https://github.com/FEniCS/${_base}"
license=(MIT)
depends=(python-setuptools python-fenics-ufl python-fenics-basix python-cffi)
makedepends=(python-wheel)
optdepends=('python-pygraphviz: utility to draw graph')
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('816da71315a7494ee97782d8c7d8df93d646a2f7b3e213d532b4dcdea179dc49248ac71d1ad7e6cf5d5d1010dc399c37c2eb22a773a86b6434a964b192d65072')

build() {
  cd ${_base}-${pkgver}
  python setup.py build
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" python setup.py install --prefix=/usr --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm 644 COPYING -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
