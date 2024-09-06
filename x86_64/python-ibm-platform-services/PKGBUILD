# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=platform-services-python-sdk
pkgname=python-ibm-platform-services
pkgver=0.57.0
pkgrel=1
pkgdesc="Python client library for IBM Cloud Platform Services"
arch=(any)
url=https://github.com/IBM/platform-services-python-sdk
license=(Apache-2.0)
depends=(
    python-ibm-cloud-sdk-core
)
makedepends=(
    python-build
    python-installer
    python-setuptools
    python-wheel
)
# We can uncomment when urllib3 is updated in [extra]
#checkdepends=(
#    python-pytest
#    python-responses
#    'python-urllib3>=2.1.0'
#)
source=($_pkgname-$pkgver.tar.gz::https://github.com/IBM/$_pkgname/archive/refs/tags/v$pkgver.tar.gz)
b2sums=('1b7dc36bf1e547e150fce0e7b80a0be8b9f4f08730856c82645a764f387624bdfe77b23621a22b7b82f8d17ce484c98662a9a43420785ab5f5964a7a83996352')

build() {
    cd $_pkgname-$pkgver
    python -m build --wheel --no-isolation
}

#check() {
#    local _site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
#    cd $_pkgname-$pkgver
#    python -m installer --destdir=test_dir dist/*.whl
#    PYTHONPATH="test_dir/$_site_packages:$PYTHONPATH" pytest test/unit
#}

package() {
    cd $_pkgname-$pkgver
    python -m installer --destdir="$pkgdir" dist/*.whl
}
