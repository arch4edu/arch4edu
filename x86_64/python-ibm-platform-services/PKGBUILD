# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=platform-services-python-sdk
pkgname=python-ibm-platform-services
pkgver=0.53.6
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
b2sums=('b8ec72934995cd5bd0303082e7629476d75b17e6eca0dc2c7a400c4b0c5e4d2db875015710300d74510ddab09ff442448db2acb8ff258e2f366f8979705adca3')

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
