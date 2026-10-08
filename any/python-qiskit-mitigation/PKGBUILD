# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-mitigation
pkgname=python-${_pkgname}
pkgver=0.1.1
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
b2sums=('248c9dec6735faa9e40d894fc8ccf2757ac3a45390520aa74ecb3d97bc3287b51b99d03e0dc10c5d46a81a4b2cc09e5c7da893ce08e3fb3d308d44e7f666b763')

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
