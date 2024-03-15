# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
pkgname=python-rustworkx
_name=${pkgname#python-}
pkgver=0.14.2
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
b2sums=('479510c4e132eda5af7a0301e760fe05daa26dd88c3299ca159ce0f87744d63cebfa33b6a1a6b43541b4c22607ea78352f36288e50d3f6535a6337be4edbf5c6')

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
}
