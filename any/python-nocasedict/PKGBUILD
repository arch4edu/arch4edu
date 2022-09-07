# Maintainer: Shalygin Konstantin <k0ste@k0ste.ru>
# Contributor: Shalygin Konstantin <k0ste@k0ste.ru>

_name='nocasedict'
pkgname="python-${_name}"
pkgver='1.0.4'
pkgrel='1'
pkgdesc='A case-insensitive ordered dictionary for Python'
arch=('any')
url="https://github.com/pywbem/${_name}"
depends=('python-six')
makedepends=('python' 'python-setuptools' 'python-wheel')
license=('GPLv2.1+')
source=("${url}/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('f86fa6978ec715c9bdb832feb8d613443125fe06c27ec87a932c1758efaa7325')

package() {
  cd "${srcdir}/${_name}-${pkgver}"
  python setup.py install -O1 --root="${pkgdir}"
}
