# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-ibm-runtime
pkgname=python-${_pkgname}
pkgver=0.44.0
pkgrel=1
pkgdesc="IBM Client for Qiskit Runtime"
arch=(any)
url=https://github.com/Qiskit/qiskit-ibm-runtime
license=(Apache-2.0)
depends=(
    blas-openblas
    python-dateutil
    python-ibm-platform-services
    python-packaging
    python-pydantic
    python-qiskit
    python-qiskit-aer
    python-requests
    python-requests-ntlm
    python-urllib3
)
optdepends=('python-plotly: interactive plots')
makedepends=(
    python-build
    python-installer
    python-setuptools
    python-setuptools-scm
    python-wheel
)
checkdepends=(
    python-ddt
    python-plotly
    python-pytest
)
source=($_pkgname-$pkgver.tar.gz::https://github.com/Qiskit/$_pkgname/archive/$pkgver.tar.gz)
b2sums=('907fc2a6e13575072d1fd9c4b938f47931488af53bd1c2f2f4bc74056ab1d20b11a89627df1aa894876c6a376b492df3ebba0ab91a37926e581d3dc6477c6ef7')

build() {
    cd $_pkgname-$pkgver
    export SETUPTOOLS_SCM_PRETEND_VERSION=$pkgver
    python -m build --wheel --no-isolation
}

check() {
    cd $_pkgname-$pkgver
    local _site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
    python -m installer --destdir=../test_dir dist/*.whl
    PYTHONPATH="$PWD/../test_dir$_site_packages" pytest test/unit
}

package() {
    cd $_pkgname-$pkgver
    python -m installer --destdir="$pkgdir" dist/*.whl
}
