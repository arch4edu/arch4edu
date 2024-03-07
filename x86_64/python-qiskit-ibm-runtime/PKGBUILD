# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-ibm-runtime
pkgname=python-${_pkgname}
pkgver=0.21.1
pkgrel=1
pkgdesc="IBM Client for Qiskit Runtime"
arch=('any')
url="https://github.com/Qiskit/qiskit-ibm-runtime"
license=('Apache-2.0')
depends=(
    'python-dateutil'
    'python-ibm-platform-services'
    'python-numpy'
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
b2sums=('5dc2d82e5d21a21d6a29a2aa005fe843d1d4467e4a23cc09c2d92c8a1604fd3ec6ec7a30a0473b2b986498d98e507ed3b23d2d966cd72f71b5c3d32f38fe1ac5')

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
