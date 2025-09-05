# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-algorithms
pkgname=python-$_pkgname
pkgver=0.4.0
pkgrel=1
pkgdesc="A library of quantum algorithms for Qiskit"
arch=(any)
url="https://github.com/qiskit-community/qiskit-algorithms"
license=(Apache-2.0)
depends=(
    python-qiskit
    python-numpy
    python-scipy
)
makedepends=(
    python-build
    python-installer
    python-setuptools
    python-wheel
)
checkdepends=(
    python-ddt
    python-pytest
)
source=(
    $_pkgname-$pkgver.tar.gz::https://github.com/qiskit-community/$_pkgname/archive/refs/tags/$pkgver.tar.gz
    fix-adaptvqe.patch::https://patch-diff.githubusercontent.com/raw/qiskit-community/qiskit-algorithms/pull/247.patch
)
b2sums=('6a09aeebb53dee0814e8ac68a4f4b6b38d78cf584e36f649d72b6a5cc41aa2e3bf83ec588a268e7713d664dd9785466ca342628fea0fb58fa4a0591ea24ceda9'
        '4709ca869faa6e719e907d9c77cd53084b7ab39386f652a39195ec279e1e38d9939fdf9d6ec3822ed746f7a130307448fa7242e46ff5ff4481e6998f195b0a02')

prepare() {
    patch -Np1 -d $_pkgname-$pkgver < fix-adaptvqe.patch
}

build() {
    cd $_pkgname-$pkgver
    python -m build --wheel --no-isolation
}

check() {
    cd $_pkgname-$pkgver
    local _site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
    python -m installer --destdir=../test_dir dist/*.whl
    # test_start() from test/optimizers/test_gradient_descent.py fails due to wrongly comparing NumPy arrays
    # The other tests are nown to fail at the moment with Qiskit 2.1.x
    PYTHONPATH=../test_dir/$_site_packages pytest -k \
        "not test_start and not test_var_qte_ode_function_time_param and not test_run_d_1_time_dependent and not test_time_dependent_hamiltonian"
}

package() {
    cd $_pkgname-$pkgver
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -D -m644 LICENSE.txt "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}
