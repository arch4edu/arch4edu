# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-finance
pkgname=python-${_pkgname}
pkgver=0.4.1
pkgrel=1
pkgdesc="Quantum Finance package for IBM qiskit framework"
arch=('any')
url="https://github.com/qiskit-community/qiskit-finance"
license=('Apache-2.0')
depends=(
    'python-certifi'
    'python-fastdtw'
    'python-nasdaq-data-link'
    'python-numpy'
    'python-pandas'
    'python-psutil'
    'python-qiskit'
    'python-qiskit-algorithms'
    'python-qiskit-optimization'
    'python-scipy'
    'python-urllib3'
    'python-yfinance'
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
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/qiskit-community/${_pkgname}/archive/${pkgver}.tar.gz")
b2sums=('2258bf0d30b5ad46e610e3adcc823da6ae50f3601e7e4ef5e39e41a3e3edbd8e58b3b8cfbee4b82ca5214952c2cdbc23448dcb64a6cfbe7e5a0746e56956497b')

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
