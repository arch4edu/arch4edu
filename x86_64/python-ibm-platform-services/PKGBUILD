# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=platform-services-python-sdk
pkgname=python-ibm-platform-services
pkgver=0.53.2
pkgrel=1
pkgdesc="Python client library for IBM Cloud Platform Services"
arch=(any)
url=https://github.com/IBM/platform-services-python-sdk
license=('Apache-2.0')
depends=(
    'python'
    'python-ibm-cloud-sdk-core'
)
makedepends=(
    'python-build'
    'python-installer'
    'python-setuptools'
    'python-wheel'
)
checkdepends=(
    'python-pytest'
    'python-responses'
    'python-urllib3>=2.1.0'
)
source=($_pkgname-$pkgver.tar.gz::https://github.com/IBM/$_pkgname/archive/refs/tags/v$pkgver.tar.gz)
b2sums=('fdb465f5f9a3c18ddcecf76b884c1829cd40c03646526f1513388fc41c38150f7f1c5b803dea2110eb76f1c3542e3eb574e56fa9d16a264ba504ed99290c1dad')

build() {
    cd $_pkgname-$pkgver
    python -m build --wheel --no-isolation
}

check() {
    local _site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
    cd $_pkgname-$pkgver
    python -m installer --destdir=test_dir dist/*.whl
    PYTHONPATH=test_dir/$_site_packages:$PYTHONPATH pytest test/unit
}

package() {
    cd $_pkgname-$pkgver
    python -m installer --destdir="$pkgdir" dist/*.whl
}
