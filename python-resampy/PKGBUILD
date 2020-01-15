# Maintainer: Jingbei Li <i@jingbei.li>
# Contributer: Jose Riha <jose1711 gmail com>
pkgname=python-resampy
_pkgname=resampy
pkgver=0.2.2
pkgrel=1
pkgdesc="Efficient sample rate conversion in python"
arch=('any')
url="https://github.com/bmcfee/resampy"
license=('ISC')
depends=('python-numba' 'python-numpy' 'python-scipy' 'python-six')
makedepends=('cython' 'python-setuptools')
source=("$url/archive/${pkgver}.tar.gz")
md5sums=('a22d712da12f17ec6fa561e5525c72f0')

build() {
  msg "Building Python 3"
  cd "$srcdir/${_pkgname}-${pkgver}"
  python setup.py build_ext -i
}

package() {
  cd "$srcdir/${_pkgname}-${pkgver}"
  python setup.py install --root="$pkgdir"/ --optimize=1
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

# vim:set ts=2 sw=2 et:
