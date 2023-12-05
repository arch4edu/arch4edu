# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-nature
pkgname=python-${_pkgname}
pkgver=0.7.1
pkgrel=1
pkgdesc="Quantum Nature package for IBM qiskit framework"
arch=('x86_64')
url="https://github.com/qiskit-community/qiskit-nature"
license=('Apache')
depends=(
    'python-h5py'
    'python-numpy'
    'python-psutil'
    'python-qiskit'
    'python-qiskit-algorithms'
    'python-rustworkx'
    'python-scipy'
    'python-typing_extensions'
)
makedepends=(
    'python-build'
    'python-installer'
    'python-setuptools'
    'python-wheel'
)
checkdepends=(
    'python-ddt'
    'python-pytest'
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/qiskit-community/${_pkgname}/archive/refs/tags/${pkgver}.tar.gz")
b2sums=('c7abc4e1f6bc5763ea2c1b154fe5ab06523b2ced85ccbd648bba128fc4015b0a4de43c4f47e902ad0e88c1ad041e3053c70a9ac6d6605d0a8fd41c328ffd9af1')

build() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m build --wheel --no-isolation
}

check() {
    local _site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
    cd "${_pkgname}-${pkgver}"
    python -m installer --destdir=test_dir dist/*.whl
    PYTHONPATH="test_dir/$_site_packages:$PYTHONPATH" pytest
}

package() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -D -m644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
