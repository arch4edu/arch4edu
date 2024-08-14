# Contributor: Patrick Mischke

pkgname='python-ibm-cloud-sdk-core'
_name='ibm-cloud-sdk-core'
pkgver=3.20.6
pkgrel=2
pkgdesc="Core python functionality required by the IBM Cloud OpenAPI SDK Generator"
url="https://github.com/IBM/python-sdk-core"
depends=('python-requests' 'python-dateutil' 'python-pyjwt')
makedepends=(python-build python-installer python-wheel python-setuptools)
license=('Apache-2.0')
arch=('any')
source=("https://github.com/IBM/python-sdk-core/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('72d8d2b6ca23fd365007d292974891b38637d1ffdc0168fbb55581ff2ba8acd9')

build() {
  cd "python-sdk-core-$pkgver"
  python -m build --wheel --no-isolation
}

package() {
  cd "python-sdk-core-$pkgver"
  python -m installer --destdir="$pkgdir" dist/*.whl
}
