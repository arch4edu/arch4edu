# Contributor: Patrick Mischke

pkgname='python-ibm-cloud-sdk-core'
_name='ibm-cloud-sdk-core'
pkgver=3.20.0
pkgrel=1
pkgdesc="Core python functionality required by the IBM Cloud OpenAPI SDK Generator"
url="https://github.com/IBM/python-sdk-core"
depends=('python-requests' 'python-dateutil' 'python-pyjwt')
makedepends=('python-setuptools')
license=('Apache-2.0')
arch=('any')
#source=("https://files.pythonhosted.org/packages/source/${_name::1}/$_name/$_name-$pkgver.tar.gz")
source=("https://github.com/IBM/python-sdk-core/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('9d7637b7f70a0b4805cfa3c02213c42ebb48baa64020f6559221733c79b1291e')

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
