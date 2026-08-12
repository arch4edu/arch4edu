# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-ibm-runtime
pkgname=python-${_pkgname}
pkgver=0.49.0
pkgrel=1
pkgdesc="IBM Client for Qiskit Runtime"
arch=(any)
url=https://github.com/Qiskit/qiskit-ibm-runtime
license=(Apache-2.0)
depends=(
    blas-openblas
    python-dateutil
    python-ibm-platform-services
    python-ibm-quantum-schemas
    python-numpy
    python-pybase64
    python-pydantic
    python-qiskit
    python-qiskit-aer
    python-requests
    python-requests-ntlm
    python-samplomatic
    python-scipy
    python-urllib3
)
optdepends=(
    "python-plotly: interactive plots"
    "python-qiskit-aer: support for simulator and noise models"
)
makedepends=(
    git
    python-build
    python-installer
    python-setuptools
    python-setuptools-scm
)
checkdepends=(
    python-ddt
    python-plotly
    python-pytest
    python-responses
)
source=($_pkgname::git+https://github.com/Qiskit/$_pkgname.git#tag=$pkgver)
b2sums=('f67faea0a15a028dbaaa2a136afe90bc0fdd9f1fa0598bdd11649770430014570ff3a77d746ed10a718eae5509424a7648e278b0d0c24279847725f099e58f09')

build() {
    cd $_pkgname
    export SETUPTOOLS_SCM_PRETEND_VERSION=$pkgver
    python -m build --wheel --no-isolation
}

check() {
    cd $_pkgname
    python -m venv --system-site-packages test-env
    test-env/bin/python -m installer dist/*.whl
    rm -rf ${_pkgname//-/_}
    test-env/bin/python -P -m pytest -o addopts="" test/unit
}

package() {
    cd $_pkgname
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -Dm644 LICENSE.txt "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}
