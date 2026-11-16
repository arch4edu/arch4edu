# Contributor: Patrick Mischke

pkgname='python-ibm-cloud-sdk-core'
_name='ibm-cloud-sdk-core'
pkgver=3.28.1
pkgrel=1
pkgdesc="Core python functionality required by the IBM Cloud OpenAPI SDK Generator"
url="https://github.com/IBM/python-sdk-core"
depends=('python-requests' 'python-dateutil' 'python-pyjwt')
makedepends=(python-build python-installer python-wheel python-setuptools)
license=('Apache-2.0')
arch=('any')
source=("https://github.com/IBM/python-sdk-core/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('2a213bca1d5d4de357127e40620031d52949091a9b83c797b61209db9f6d46e2')

build() {
  cd "python-sdk-core-$pkgver"
  python -m build --wheel --no-isolation
}

package() {
  cd "python-sdk-core-$pkgver"
  python -m installer --destdir="$pkgdir" dist/*.whl
}
