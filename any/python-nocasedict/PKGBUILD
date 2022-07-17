# Maintainer: Shalygin Konstantin <k0ste@k0ste.ru>
# Contributor: Shalygin Konstantin <k0ste@k0ste.ru>

_name='nocasedict'
pkgname="python-${_name}"
pkgver='1.0.3'
pkgrel='1'
pkgdesc='A case-insensitive ordered dictionary for Python'
arch=('any')
url="https://github.com/pywbem/${_name}"
depends=('python-six')
makedepends=('python' 'python-setuptools' 'python-wheel')
license=('GPLv2.1+')
source=("${url}/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('f3314c02f4b9a0c194991c585d7e793e367e041a78efe0cbfc1a3d4362a91d5b')

package() {
  cd "${srcdir}/${_name}-${pkgver}"
  python setup.py install -O1 --root="${pkgdir}"
}
