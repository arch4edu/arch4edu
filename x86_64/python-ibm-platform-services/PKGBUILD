# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=platform-services-python-sdk
pkgname=python-ibm-platform-services
pkgver=0.28.1
pkgrel=1
pkgdesc="Python client library for IBM Cloud Platform Services"
arch=('any')
url="https://github.com/IBM/platform-services-python-sdk"
license=('Apache')
depends=(
    'python-dateutil'
    'python-ibm-cloud-sdk-core'
    'python-requests'
    'python-urllib3'
)
makedepends=(
    'python-build'
    'python-installer'
    'python-setuptools'
    'python-wheel'
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/IBM/${_pkgname}/archive/refs/tags/v${pkgver}.tar.gz")
b2sums=('17c350009ed3fdba9bb80c7bbf37fe5c36918e05e80e322552b6c5f49577ae6ae7354fcc1ab938afa5b6fe28b794549e9c22261875d6bfaf8218a1175e4ff3f1')

build() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m build --wheel --no-isolation
}

package() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m installer --destdir="$pkgdir" dist/*.whl
}
