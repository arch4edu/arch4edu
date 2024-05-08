# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-ibm-provider
pkgname=python-${_pkgname}
pkgver=0.11.0
pkgrel=1
pkgdesc="Qiskit Provider for accessing the IBM Quantum Services: Online Systems and Simulators"
arch=(any)
url=https://github.com/Qiskit/qiskit-ibm-provider
license=(Apache-2.0)
depends=(
    python-dateutil
    python-numpy
    python-qiskit
    python-requests
    python-requests-ntlm
    python-typing_extensions
    python-urllib3
    python-websocket-client
    python-websockets
)
makedepends=(
    python-build
    python-installer
    python-setuptools
    python-wheel
)
#checkdepends=(
#    jupyter-nbformat
#    python-ddt
#    python-ipywidgets
#    python-pytest
#    python-qiskit-aer
#    python-qiskit-ibm-runtime
#)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/Qiskit/${_pkgname}/archive/refs/tags/${pkgver}.tar.gz")
b2sums=('ef2f11e06e03addb7bb1c98d298fa6742b89e178c81a773c72218e5aae7130175708823dca4bf79e45b1712a1debb533efa280698f426ed2fc5857c7d99cbdd4')

build() {
    cd "${_pkgname}-${pkgver}"
    python -m build --wheel --no-isolation
}

#check() {
#    cd $_pkgname-$pkgver
#    local _site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
#    python -m installer --destdir=../test_dir dist/*.whl
#    PYTHONPATH=../test_dir/$_site_packages pytest
#}

package() {
    cd "${_pkgname}-${pkgver}"
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -D -m644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
