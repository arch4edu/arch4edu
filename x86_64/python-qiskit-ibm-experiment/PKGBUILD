# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-ibm-experiment
pkgname=python-${_pkgname}
pkgver=0.4.8
pkgrel=1
pkgdesc="Service that allows accessing the IBM Quantum experiment database."
arch=(any)
url=https://github.com/Qiskit-Extensions/qiskit-ibm-experiment
license=(Apache-2.0)
depends=(
    python-pandas
    python-qiskit
    python-requests
    python-requests-ntlm
    python-urllib3
    python-yaml
)
makedepends=(
    python-build
    python-installer
    python-setuptools
    python-wheel
)
#checkdepends=(
#    python-fixtures
#    python-pytest
#    python-testtools
#)
source=($_pkgname-$pkgver.tar.gz::https://github.com/Qiskit-Extensions/$_pkgname/archive/$pkgver.tar.gz)
b2sums=('394dc071a4444c70afeddf0ac5a46b011b97faf15b24df890c2fbac2a66a45b0a65e18f40777011831eeb1a9003664a1294f94d9c0f2b698bd0aa594235c05ea')

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
