# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-ibm-runtime
pkgname=python-${_pkgname}
pkgver=0.22.0
pkgrel=1
pkgdesc="IBM Client for Qiskit Runtime"
arch=('any')
url="https://github.com/Qiskit/qiskit-ibm-runtime"
license=('Apache-2.0')
depends=(
    'python-dateutil'
    'python-ibm-platform-services'
    'python-numpy'
    'python-pydantic'
    'python-qiskit'
    'python-requests'
    'python-requests-ntlm'
    'python-scipy'
    'python-typing_extensions'
    'python-urllib3'
    'python-websocket-client'
)
makedepends=(
    'python-build'
    'python-installer'
    'python-setuptools'
    'python-wheel'
)
#checkdepends=(
#    'jupyter-nbconvert'
#    'python-ddt'
#    'python-psutil'
#    'python-pytest'
#    'python-qiskit-aer'
#    'python-websockets'
#)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/Qiskit/${_pkgname}/archive/${pkgver}.tar.gz")
b2sums=('337d5fa31f22ca103cf08c2eb4988d9d2efea43c703e88eff11d646b0f5c22de468c0358bc27a1dc27880eeec1abcba87afa27bd5e39a2574eee2cf747888b23')

build() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m build --wheel --no-isolation
}

#check() {
#    local _site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
#    cd "${_pkgname}-${pkgver}"
#    python -m installer --destdir=test_dir dist/*.whl
#    PYTHONPATH="test_dir/$_site_packages:$PYTHONPATH" pytest
#}

package() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m installer --destdir="$pkgdir" dist/*.whl
}
