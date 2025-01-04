# Maintainer: Martin Diehl <aur@martin-diehl.net>

pkgname=python-scooby
pkgver=0.10.0
pkgrel=5
pkgdesc='A Great Dane turned Python environment detective'
arch=(any)
url=https://github.com/banesullivan/scooby
license=(MIT)
depends=(python)
makedepends=(python-build python-installer python-wheel python-setuptools-scm)
_name=${pkgname#python-}
source=(https://github.com/banesullivan/${_name}/archive/v${pkgver}/${_name}-${pkgver}.tar.gz)
sha512sums=('1f47f90ec0061e411fd5808868307d20aabd82cee1afd0036e9dc8f41d7014d4b3032c0c9da4ec35b76d9420203cb24377bea0cff7d19a822208197d9f8550d3')

prepare() {
    sed -i "11i version=\'${pkgver}\',"  ${_name}-${pkgver}/setup.py
}

build() {
    cd ${_name}-${pkgver}
    python -m build --wheel --no-isolation
}

package() {
    cd ${_name}-${pkgver}
    python -m installer --destdir="${pkgdir}" dist/*.whl
    install -Dm644 LICENSE -t "${pkgdir}"/usr/share/licenses/${pkgname}
}
