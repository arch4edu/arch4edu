# Contributor: Patrick Mischke

pkgname='python-ibm-cloud-sdk-core'
_name='ibm-cloud-sdk-core'
pkgver=3.24.1
pkgrel=1
pkgdesc="Core python functionality required by the IBM Cloud OpenAPI SDK Generator"
url="https://github.com/IBM/python-sdk-core"
depends=('python-requests' 'python-dateutil' 'python-pyjwt')
makedepends=(python-build python-installer python-wheel python-setuptools)
license=('Apache-2.0')
arch=('any')
source=("https://github.com/IBM/python-sdk-core/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('7a80fc0678e9a7018da70dfeb3d3221444070e76bd6f4df05797c33694d7eab6')

build() {
  cd "python-sdk-core-$pkgver"
  python -m build --wheel --no-isolation
}

package() {
  cd "python-sdk-core-$pkgver"
  python -m installer --destdir="$pkgdir" dist/*.whl
}
