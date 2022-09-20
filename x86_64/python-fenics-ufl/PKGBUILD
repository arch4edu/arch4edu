# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=ufl
pkgname=python-fenics-${_base}
pkgdesc="UFL - Unified Form Language"
pkgver=2022.2.0
pkgrel=1
arch=(any)
url="https://github.com/FEniCS/${_base}"
license=(MIT)
depends=(python-numpy python-setuptools)
makedepends=(python-wheel)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/refs/tags/${pkgver}.tar.gz)
sha512sums=('45c8e603ea99af6cfcd7274fa95aa5bacb349a29390e1b8104a3123823f9f997e7a45bd1be866fd7f06f1aaba9c99681674001483702de168235b4442296f1fc')
provides=("python-${_base}")
conflicts=("python-${_base}" "python-${_base}-git")

build() {
  cd ${_base}-${pkgver}
  python setup.py build
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" python setup.py install --prefix=/usr --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm 644 COPYING -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
