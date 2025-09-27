# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-ibm-runtime
pkgname=python-${_pkgname}
pkgver=0.42.0
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
b2sums=('5632f1c330d42bb1348eb54893eb90b7871850ed01ee999b0929f2edf45c3f2a02f53beee7375f518be36a74ddab3f1ad27ef1c01211d786a12548fa57f8453b')

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
