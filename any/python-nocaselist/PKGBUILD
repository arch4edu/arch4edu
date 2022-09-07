# Maintainer: Shalygin Konstantin <k0ste@k0ste.ru>
# Contributor: Shalygin Konstantin <k0ste@k0ste.ru>

_name='nocaselist'
pkgname="python-${_name}"
pkgver='1.0.6'
pkgrel='1'
pkgdesc='A case-insensitive list for Python'
arch=('any')
url="https://github.com/pywbem/${_name}"
makedepends=('python' 'python-setuptools' 'python-wheel')
license=('GPLv2.1+')
source=("${url}/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('c462290af329193c7e43613f947563c8f7165676e69c2a3fc71bddfea15d7033')

package() {
  cd "${srcdir}/${_name}-${pkgver}"
  python setup.py install -O1 --root="${pkgdir}"
}
