# Contributor: Patrick Mischke

pkgname='python-ibm-cloud-sdk-core'
_name='ibm-cloud-sdk-core'
pkgver=3.22.1
pkgrel=1
pkgdesc="Core python functionality required by the IBM Cloud OpenAPI SDK Generator"
url="https://github.com/IBM/python-sdk-core"
depends=('python-requests' 'python-dateutil' 'python-pyjwt')
makedepends=(python-build python-installer python-wheel python-setuptools)
license=('Apache-2.0')
arch=('any')
source=("https://github.com/IBM/python-sdk-core/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('d63b10e4f9ecb64e415ce874a8f7a206c637df3f5eb7ceee36a8f5e210ff30fc')

build() {
  cd "python-sdk-core-$pkgver"
  python -m build --wheel --no-isolation
}

package() {
  cd "python-sdk-core-$pkgver"
  python -m installer --destdir="$pkgdir" dist/*.whl
}
