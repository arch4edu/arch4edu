# Maintainer: Guillaume Horel <guillaume.horel@gmail.com> 

pkgname='python-cachey'
_pkgname=cachey
pkgver=0.2.1
pkgrel=1
pkgdesc="Caching based on computation time and storage space"
arch=('any')
url="https://github.com/dask/cachey"
license=('BSD')
checkdepends=('python-nose')
depends=('python-heapdict')
makedepends=('python-setuptools')
source=("$pkgname-$pkgver.tar.gz::https://github.com/dask/cachey/archive/$pkgver.tar.gz")
sha256sums=('27242020785aec748c24428cb2f6ee30bbe116fb1a5ac18b3e64784f683dd1d4')

package(){
  cd "$srcdir/$_pkgname-$pkgver"
  install -D -m644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
  python setup.py install --root="$pkgdir/" --optimize=1
}

check(){
  cd "$srcdir/$_pkgname-$pkgver"
  nosetests
}
# vim:ts=2:sw=2:et:
