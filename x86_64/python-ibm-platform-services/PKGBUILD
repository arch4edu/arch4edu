# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=platform-services-python-sdk
pkgname=python-ibm-platform-services
pkgver=0.46.0
pkgrel=1
pkgdesc="Python client library for IBM Cloud Platform Services"
arch=('any')
url="https://github.com/IBM/platform-services-python-sdk"
license=('Apache')
depends=('python-ibm-cloud-sdk-core')
makedepends=(
    'python-build'
    'python-installer'
    'python-setuptools'
    'python-wheel'
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/IBM/${_pkgname}/archive/refs/tags/v${pkgver}.tar.gz")
b2sums=('f1622c245ce5022ff80934c3a93b68aa6d2db59f1ae951f67ed3301bb42261bbebfba966840dcc138bd7e021dd4badf2c92a663bb65e6745f8afc542ef943849')

build() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m build --wheel --no-isolation
}

package() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m installer --destdir="$pkgdir" dist/*.whl
}
