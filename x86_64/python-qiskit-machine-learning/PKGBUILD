# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-machine-learning
pkgname=python-${_pkgname}
pkgver=0.7.1
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
b2sums=('0385a83cbb1fa1dc6011b3a69aa0c3a10ccf8a6ec27294afda9d7d5e049fad1c9aaeaa5756543b0b180423da15f8e14a545f836fa05a08ab66c07bd4a3d69423')

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
