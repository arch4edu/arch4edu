# Contributor: Patrick Mischke

pkgname='python-ibm-cloud-sdk-core'
_name='ibm-cloud-sdk-core'
pkgver=3.21.0
pkgrel=1
pkgdesc="Core python functionality required by the IBM Cloud OpenAPI SDK Generator"
url="https://github.com/IBM/python-sdk-core"
depends=('python-requests' 'python-dateutil' 'python-pyjwt')
makedepends=(python-build python-installer python-wheel python-setuptools)
license=('Apache-2.0')
arch=('any')
source=("https://github.com/IBM/python-sdk-core/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('bb62279e1151389acd321601ae3c3e4e6860fa44af4510b5377a25b24e5ebdf3')

build() {
  cd "python-sdk-core-$pkgver"
  python -m build --wheel --no-isolation
}

package() {
  cd "python-sdk-core-$pkgver"
  python -m installer --destdir="$pkgdir" dist/*.whl
}
