# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-qasm3-import
pkgname=python-${_pkgname}
pkgver=0.5.1
pkgrel=1
pkgdesc="Importer from OpenQASM 3 to Qiskit's QuantumCircuit"
arch=(any)
url=https://github.com/Qiskit/qiskit-qasm3-import
license=(Apache-2.0)
depends=(
    python-openqasm3
    python-qiskit
)
makedepends=(
    python-build
    python-installer
    python-setuptools
    python-wheel
)
checkdepends=(python-pytest)
source=($_pkgname-$pkgver.tar.gz::https://github.com/Qiskit/$_pkgname/archive/refs/tags/v$pkgver.tar.gz)
b2sums=('3ff57dac3bacdd15aeec72010252f811b99a42efd0243bfd28c2fcc9c481c34a67426065f6f0d1e981172c7ff8b203b8a42ccb46a8eec668c5c8d5dde3854d49')

build() {
    cd $_pkgname-$pkgver
    python -m build --wheel --no-isolation
}

check() {
    cd $_pkgname-$pkgver
    local _site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
    python -m installer --destdir=../test_dir dist/*.whl
    PYTHONPATH="$PWD/../test_dir/$_site_packages" pytest tests
}

package() {
    cd $_pkgname-$pkgver
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -D -m644 LICENSE "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}
