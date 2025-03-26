# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=platform-services-python-sdk
pkgname=python-ibm-platform-services
pkgver=0.63.0
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
b2sums=('a664fc0a058dcfa5f2d0fe5d99494464214e43aaa5e4da0566d967a05010740c22ac24c8ad30fee11baa9228b97765e249e7a3356a7974426add611e1d6a1934')

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
