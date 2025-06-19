# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-qasm3-import
pkgname=python-${_pkgname}
pkgver=0.6.0
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
b2sums=('be426173c8e3641d4460bba88e37b4f32b04b10291c1fbc1347d013675eb80068204c9e1cbf86e9f7bcba08450c8be0125fcc97ab2c5b5ad0be00f3d4d126d08')

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
