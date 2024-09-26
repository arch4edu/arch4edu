# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-ibm-runtime
pkgname=python-${_pkgname}
pkgver=0.30.0
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
optdepends=(
    'python-plotly: interactive plots'
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
b2sums=('9019d9bf982816782b95108af172dd0baec74420538c3c056192a99ef78b792b9bb21bc115a0e3ee7179ccf270c5a68e1fb2ee633e2284b5b3d171afd882c653')

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
