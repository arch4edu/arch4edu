# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_name=rustworkx
pkgname=python-$_name
pkgver=0.16.0
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
    python-setuptools
    python-setuptools-rust
    python-wheel
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
b2sums=('ad3e8755ac2705010cf87d6613b8a06361645e1ebde34a62a98f08452afb99155cda8a16f7222a37dda299369e8b887f1d8683c07b1ce2b5169af06a3866474c')

build() {
    cd $_name-$pkgver
    python -m build --wheel --no-isolation
}

check() {
    cd $_name-$pkgver
    local python_version=$(python -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
    python -m installer --destdir=../test_dir dist/*.whl
    rm -rf $_name
    PYTHONPATH="$PWD/../test_dir/usr/lib/python$python_version/site-packages" pytest tests
}

package() {
    cd $_name-$pkgver
    python -m installer --destdir="$pkgdir" dist/*.whl
}
