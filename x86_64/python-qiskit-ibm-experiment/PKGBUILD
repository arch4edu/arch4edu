# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-ibm-experiment
pkgname=python-${_pkgname}
pkgver=0.4.8
pkgrel=2
pkgdesc="Service that allows accessing the IBM Quantum experiment database."
arch=(any)
url=https://github.com/qiskit-community/qiskit-ibm-experiment
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
# checkdepends=(
#     python-fixtures
#     python-ibm-cloud-sdk-core
#     python-pytest
#     python-qiskit-ibm-runtime
#     python-testtools
# )
source=($_pkgname-$pkgver.tar.gz::https://github.com/qiskit-community/$_pkgname/archive/$pkgver.tar.gz)
b2sums=('63c40d1c4a86b7f80dbdb4ad35e733fe906b13c6885b9383374ffd846b2a282638e0887e9a1196c3ae8328f4972e79dd52ec5e01da51cec9504d68328d043ac8')

build() {
    cd $_pkgname-$pkgver
    python -m build --wheel --no-isolation
}

# check() {
#     cd $_pkgname-$pkgver
#     local _site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
#     python -m installer --destdir=../test_dir dist/*.whl
#     PYTHONPATH=../test_dir/$_site_packages pytest
# }

package() {
    cd $_pkgname-$pkgver
    python -m installer --destdir="$pkgdir" dist/*.whl
}
