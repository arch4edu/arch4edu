# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
pkgname=python-rustworkx
_name=${pkgname#python-}
pkgver=0.14.0
pkgrel=1
pkgdesc="A high performance Python graph library implemented in Rust"
arch=("x86_64")
url="https://github.com/Qiskit/rustworkx"
license=('Apache-2.0')
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
b2sums=('aad2c95f5e3fee6939cbfc53b81197b5fd149925a3be683a09412c5f2d0b32da90ed06d5efb5f24b6f77138074fb4234d16296119890c9e15a8d3002c2112638')

build() {
    cd "${_name}-${pkgver}"
    python -m build --wheel --no-isolation
}

check() {
    local _site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
    cd "${_name}-${pkgver}"
    rm -rf test rustworkx
    python -m installer --destdir=test_dir dist/*.whl
    # The 3 tests configured not to run halt the system indefinitely
    PYTHONPATH="test_dir/${_site_packages}:${PYTHONPATH}" pytest -v -k "not test_edge_colormap and not test_labels_and_colors and not test_node_list"
}

package() {
    cd "${_name}-${pkgver}"
    python -m installer --destdir="${pkgdir}" dist/*.whl
    install -D -m644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
