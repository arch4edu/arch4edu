# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
pkgname=python-rustworkx
_name=${pkgname#python-}
pkgver=0.13.2
pkgrel=1
pkgdesc="A high performance Python graph library implemented in Rust"
arch=("x86_64")
url="https://github.com/Qiskit/rustworkx"
license=('Apache')
depends=('python-numpy')
optdepends=(
    'graphviz: graphviz based drawer function'
    'python-matplotlib: matplotlib based drawer function'
    'python-pillow: also required for graphviz based drawer function'
)
makedepends=(
    'python-build'
    'python-installer'
    'python-setuptools'
    'python-setuptools-rust'
    'python-wheel'
)
checkdepends=(
    'python-fixtures'
    'python-graphviz'
    'python-matplotlib'
    'python-networkx'
    'python-pillow'
    'python-pytest'
    'python-testtools'
)
conflicts=('python-retworkx')
source=("${_name}-${pkgver}.tar.gz::https://github.com/Qiskit/${_name}/archive/refs/tags/${pkgver}.tar.gz")
b2sums=('77067f1ac27fd578b9e9d0e485fd5f516a7799941ff51b83eb5fb6644de328c29567c7ac2a0bea4944be5ae412f130ca12f6fd42efa57272a3cc35955399d003')

build() {
    cd "${srcdir}/${_name}-${pkgver}"
    python -m build --wheel --no-isolation
}

check() {
    cd "${srcdir}/${_name}-${pkgver}"
    rm -rf test
    python -m installer --destdir="test" dist/*.whl
    local python_version=$(python -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
    export PYTHONPATH="${PWD}/test/usr/lib/python${python_version}/site-packages"
    rm -rf rustworkx
    python -m pytest -k "not test_edge_colormap and not test_labels_and_colors and not test_node_list" tests/rustworkx_tests/
}

package() {
    cd "${srcdir}/${_name}-${pkgver}"
    python -m installer --destdir="${pkgdir}" dist/*.whl
    install -D -m644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
