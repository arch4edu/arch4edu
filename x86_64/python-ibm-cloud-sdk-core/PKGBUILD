# Contributor: Patrick Mischke

pkgname='python-ibm-cloud-sdk-core'
_name='ibm-cloud-sdk-core'
pkgver=3.20.3
pkgrel=2
pkgdesc="Core python functionality required by the IBM Cloud OpenAPI SDK Generator"
url="https://github.com/IBM/python-sdk-core"
depends=('python-requests' 'python-dateutil' 'python-pyjwt')
makedepends=('python-setuptools')
license=('Apache-2.0')
arch=('any')
source=("https://github.com/IBM/python-sdk-core/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('2132574a94c0b2022244fe1194ff3e917ad527703dba4d7bf9ae06942a45b61e')

build() {
  cd "python-sdk-core-$pkgver"
  python setup.py build
}

package() {
  cd "python-sdk-core-$pkgver"
  python setup.py install --prefix=/usr --root="${pkgdir}" --optimize=1 --skip-build
  rm -rd "${pkgdir}/usr/lib/python3.12/site-packages/test"
  rm -rd "${pkgdir}/usr/lib/python3.12/site-packages/test_integration"
}
