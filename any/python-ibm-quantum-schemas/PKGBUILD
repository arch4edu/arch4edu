# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=ibm-quantum-schemas
pkgname=python-${_pkgname}
pkgver=0.11.20260824
pkgrel=1
pkgdesc="IBM Quantum API Schemas"
arch=(any)
url=https://github.com/Qiskit/ibm-quantum-schemas
license=(Apache-2.0)
depends=(
    python-numpy
    python-pybase64
    python-pydantic
    python-qiskit
    python-qiskit-qasm3-import
    python-samplomatic
)
makedepends=(
    git
    python-build
    python-installer
    python-setuptools
    python-setuptools-scm
)
checkdepends=(python-pytest)
source=($_pkgname::git+https://github.com/Qiskit/$_pkgname.git#tag=$pkgver)
b2sums=('37e967f4b691d9e4cbd1e5833ba207d532311db8cfaaece47a12947e5ddceb2ab72b7a022413b20b093a49d68ce66ca1e2593b366a03c366e094d68b0aae878d')

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
