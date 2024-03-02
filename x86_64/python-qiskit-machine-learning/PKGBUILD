# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-machine-learning
pkgname=python-${_pkgname}
pkgver=0.7.2
pkgrel=1
pkgdesc="Quantum Machine Learning package for IBM qiskit framework"
arch=('x86_64')
url="https://github.com/qiskit-community/qiskit-machine-learning"
license=('Apache')
depends=(
    'python-dill'
    'python-fastdtw'
    'python-numpy'
    'python-psutil'
    'python-qiskit'
    'python-qiskit-algorithms'
    'python-scikit-learn'
    'python-scipy'
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
b2sums=('275a0a7e2340b14f5e00af5f668dff56ea410a5ed4cdc4df3247ad5fd1a582efd171a90fd17cb1bb58700b6bbb5d0654bcd50206a98a350e79ad7744b6100fda')

build() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m build --wheel --no-isolation
}

check() {
    local _site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
    cd "${_pkgname}-${pkgver}"
    python -m installer --destdir=test_dir dist/*.whl
    # Some tests fail: https://github.com/qiskit-community/qiskit-machine-learning/issues/726
    PYTHONPATH="test_dir/$_site_packages:$PYTHONPATH" pytest \
        -k 'not test_save_load and not test_change_kernel and not test_qsvr'
}

package() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -D -m644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
