# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_name=rustworkx
pkgname=python-$_name
pkgver=0.18.1
pkgrel=1
pkgdesc="A high performance Python graph library implemented in Rust"
arch=(x86_64)
url=https://github.com/Qiskit/rustworkx
license=(Apache-2.0)
depends=(python-numpy)
optdepends=(
    'graphviz: graphviz based drawer function'
    'python-matplotlib: matplotlib based drawer function'
    'python-pillow: also required for graphviz based drawer function'
)
makedepends=(
    python-build
    python-installer
    python-maturin
)
checkdepends=(
    python-fixtures
    python-graphviz
    python-matplotlib
    python-networkx
    python-pillow
    python-pytest
    python-testtools
)
conflicts=(python-retworkx)
source=($_name-$pkgver.tar.gz::https://github.com/Qiskit/$_name/archive/refs/tags/$pkgver.tar.gz)
b2sums=('e93eb0a940a446165c60d521aeb7503c2f42b65723e027b05f01700c1da22c21620f2480ac1ef63ec2dc13d66ffe3f2720685474a685d0e4e262aeed483f708d')

build() {
    cd $_name-$pkgver
    python -m build --wheel --no-isolation
}

check() {
    cd $_name-$pkgver
    python -m venv --system-site-packages test-env
    test-env/bin/python -m installer dist/*.whl
    rm -rf $_name
    test-env/bin/python -P -m pytest -o addopts=""
}

package() {
    cd $_name-$pkgver
    python -m installer --destdir="$pkgdir" dist/*.whl
}
