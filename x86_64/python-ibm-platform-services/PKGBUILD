# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=platform-services-python-sdk
pkgname=python-ibm-platform-services
pkgver=0.55.1
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
b2sums=('a5acf8bf5c5757d691d0b77808e18bf2be734b038530e5bcb5b85db2098863683d649034ce38ea70f0e52aa2619f4138f3d28e4f1cf2f4033e30c96b3064d415')

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
