# Maintainer: Jingbei Li <i@jingbei.li>
# Contributer: Jose Riha <jose1711 gmail com>
pkgname=python-resampy
_pkgname=resampy
pkgver=0.4.1
pkgrel=1
pkgdesc="Efficient sample rate conversion in python"
arch=('any')
url="https://github.com/bmcfee/resampy"
license=('ISC')
depends=('python-numba' 'python-numpy')
makedepends=('python-setuptools')
#checkdepends=('python-scipy')
source=("$url/archive/${pkgver}.tar.gz")
md5sums=('e176c3b79ae9041cd5f6928377b656b5')

build() {
  cd "$srcdir/${_pkgname}-${pkgver}"
  python setup.py build_ext -i
}

package() {
  cd "$srcdir/${_pkgname}-${pkgver}"
  python setup.py install --root="$pkgdir"/ --optimize=1
  install -Dm644 LICENSE.md "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

# vim:set ts=2 sw=2 et:
