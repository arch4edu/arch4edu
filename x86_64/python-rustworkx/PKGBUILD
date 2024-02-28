# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
pkgname=python-rustworkx
_name=${pkgname#python-}
pkgver=0.14.1
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
b2sums=('03ebbd55762ef3f8834ed688782580a2ffb05dc34410c9970337d776bcc52afb2ee474860cbcd173d57c3736b8562a1848df558d304de872d4f0e98522c57d46')

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
