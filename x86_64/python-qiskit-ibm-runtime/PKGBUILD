# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-ibm-runtime
pkgname=python-${_pkgname}
pkgver=0.29.0
pkgrel=1
pkgdesc="IBM Client for Qiskit Runtime"
arch=(any)
url=https://github.com/Qiskit/qiskit-ibm-runtime
license=(Apache-2.0)
depends=(
    python-dateutil
    python-ibm-platform-services
    python-numpy
    python-pydantic
    python-qiskit
    python-requests
    python-requests-ntlm
    python-scipy
    python-typing_extensions
    python-urllib3
    python-websocket-client
)
makedepends=(
    python-build
    python-installer
    python-setuptools
    python-wheel
)
#checkdepends=(
#    python-ddt
#    python-pytest
#    python-qiskit-aer
#    python-websockets
#)
source=($_pkgname-$pkgver.tar.gz::https://github.com/Qiskit/$_pkgname/archive/$pkgver.tar.gz)
b2sums=('0e8e39410eded49b66cce898a0e167a3359a8614e4658cb72ef9fb2ff2088569e1dd7cd458d817b1bbcff6a2bbcbf3f08d6bf96839189be8dea51fce60d5ffd9')

build() {
    cd $_pkgname-$pkgver
    python -m build --wheel --no-isolation
}

#check() {
#    cd $_pkgname-$pkgver
#    local _site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
#    python -m installer --destdir=../test_dir dist/*.whl
#    PYTHONPATH=../test_dir/$_site_packages pytest
#}

package() {
    cd $_pkgname-$pkgver
    python -m installer --destdir="$pkgdir" dist/*.whl
}
