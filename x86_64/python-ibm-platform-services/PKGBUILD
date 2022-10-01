# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=platform-services-python-sdk
pkgname=python-ibm-platform-services
pkgver=0.27.0
pkgrel=2
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
b2sums=('4aad57eac4befe27bfad90e3374720b8ff88c0e24d7bfbf818e15da2f18fd7b377641be834301e3000a1c346e7581604318ebddddaf4ec78a7d0a3934c3d8117')

build() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m build --wheel --no-isolation
}

package() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m installer --destdir="$pkgdir" dist/*.whl
}
