# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
pkgname=python-rustworkx
_name=${pkgname#python-}
pkgver=0.15.1
pkgrel=2
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
b2sums=('b74a892cdaf184977d05f3e99205dded6d6eebbed3cff6cde52b7832eb8945c6de51297a7dad7b4ab6ca5229d5b5b8f15c754dba8341941ff618d2826bd86a6d')

build() {
    cd $_name-$pkgver
    python -m build --wheel --no-isolation
}

check() {
    cd $_name-$pkgver
    local _site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
    python -m installer --destdir=../test_dir dist/*.whl
    # Delete src folders to be sure we test with installed package
    rm -r rustworkx retworkx
    PYTHONPATH=../test_dir/$_site_packages pytest
}

package() {
    cd $_name-$pkgver
    python -m installer --destdir="$pkgdir" dist/*.whl
}
