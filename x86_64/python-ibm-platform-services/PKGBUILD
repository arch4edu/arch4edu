# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=platform-services-python-sdk
pkgname=python-ibm-platform-services
pkgver=0.68.2
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
b2sums=('097649aa9feb3922dfd5889f39136a0056a16c68551a82c0fa7472f08a14fb78fb9f3e2ec9af43db67d2229ddfa25ce47ca211018dbe09e639a9cb774fd31872')

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
