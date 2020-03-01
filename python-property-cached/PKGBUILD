# Maintainer: Guillaume Horel <guillaume.horel@gmail.com>

pkgname=python-property-cached
_pkgname=property-cached
pkgver=1.6.3
pkgrel=1
pkgdesc="A decorator for caching properties in classes"
arch=('any')
url="https://github.com/althonos/property-cached/"
license=('BSD')
depends=('python')
optdepends=()
makedepends=('python-setuptools')
checkdepends=('python-freezegun')
source=("https://pypi.org/packages/source/${_pkgname:0:1}/$_pkgname/$_pkgname-$pkgver.zip")
sha256sums=('614b6972e279d981b7bccabd0b1ce4601c1739a6eb9905fd79a9c485fb20a1e0')

package(){
  cd "$srcdir/$_pkgname-$pkgver"
  python setup.py install --root="$pkgdir/" --optimize=1
}

check() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  python setup.py test
}
## vim:ts=2:sw=2:et:
