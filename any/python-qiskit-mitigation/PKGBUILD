# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-mitigation
pkgname=python-${_pkgname}
pkgver=0.2.0
pkgrel=1
pkgdesc="A toolbox for handling noise in quantum computations"
arch=(any)
url=https://github.com/Qiskit/qiskit-mitigation
license=(Apache-2.0)
depends=(
    python-numpy
    python-qiskit
    python-samplomatic
    python-scipy
)
makedepends=(
    git
    python-build
    python-hatchling
    python-installer
)
checkdepends=(
    python-ddt
    python-pytest
)
source=($_pkgname::git+$url.git#tag=$pkgver)
b2sums=('0c0e49951f9be2d4426017c905b66a179874d356cfc4f030a8b8cba2c0fb712dcf2708a67a5630809ae6cc5c73eec0baac07597b288c522eede348ba9b31ccea')

build() {
    cd $_pkgname
    python -m build --wheel --no-isolation
}

check() {
    cd $_pkgname
    python -m venv --system-site-packages test-env
    test-env/bin/python -m installer dist/*.whl
    rm -rf ${_pkgname//-/_}
    test-env/bin/python -P -m pytest -o addopts=""
}

package() {
    cd $_pkgname
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -Dm644 LICENSE.txt "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}
