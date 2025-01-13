# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=platform-services-python-sdk
pkgname=python-ibm-platform-services
pkgver=0.59.1
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
checkdepends=(
   python-pytest
   python-responses
   python-urllib3
)
source=($_pkgname-$pkgver.tar.gz::https://github.com/IBM/$_pkgname/archive/refs/tags/v$pkgver.tar.gz)
b2sums=('ef6728d805bce9a9f633080c940f99f2840ccab43f86c3b2ad3b9c39e3f0dfb7845c57a431e610ffc8f50bc2d7f0955c95d151b182252563482677d1d1f61cf8')

build() {
    cd $_pkgname-$pkgver
    python -m build --wheel --no-isolation
}

check() {
   local _site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
   cd $_pkgname-$pkgver
   rm -r ibm_platform_services
   python -m installer --destdir=test_dir dist/*.whl
   PYTHONPATH="test_dir/$_site_packages:$PYTHONPATH" pytest test/unit
}

package() {
    cd $_pkgname-$pkgver
    python -m installer --destdir="$pkgdir" dist/*.whl
}
