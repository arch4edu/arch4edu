# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-ibm-runtime
pkgname=python-${_pkgname}
pkgver=0.52.1
pkgrel=1
pkgdesc="IBM Client for Qiskit Runtime"
arch=(any)
url=https://github.com/Qiskit/qiskit-ibm-runtime
license=(Apache-2.0)
depends=(
    python-dateutil
    python-ibm-platform-services
    python-ibm-quantum-schemas
    python-numpy
    python-pybase64
    python-pydantic
    python-qiskit
    python-qiskit-aer
    python-qiskit-mitigation
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
b2sums=('601faacd129b4213ad121cfb6db381bdcaf23e5e1f60041f396c36ab0de550ffed20af8179798068c294e9367af767746fcc0f299633ac63ea73b9d3206bbd53')

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
