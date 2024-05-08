# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-ibm-experiment
pkgname=python-${_pkgname}
pkgver=0.4.7
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
b2sums=('4a824e46fb4f6c1ab0f4ec7a1c90e051ef8cfbe4b79845bb8e26b4d75769b674b79887ff114f2d9776f032efcf17a7da51b01a12474ebc9a96b5e7b822c0c62d')

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
