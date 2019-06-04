# Maintainer: Guillaume Horel <guillaume.horel@gmail.com> 

pkgbase=python-cachey
pkgname=('python-cachey' 'python2-cachey')
_pkgname=cachey
pkgver=0.1.1
pkgrel=1
pkgdesc="Caching based on computation time and storage space"
arch=('any')
url="https://github.com/dask/cachey"
license=('BSD')
checkdepends=('python-nose' 'python2-nose')
makedepends=('python-setuptools' 'python2-setuptools' 'git')
source=("git+https://github.com/dask/cachey.git#commit=6d4aca7")
sha256sums=('SKIP')

prepare() {
  cp -a $_pkgname{,-py2}
}

package_python-cachey(){
  depends=('python-heapdict')
  cd "$srcdir/$_pkgname"
  install -D -m644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
  python setup.py install --root="$pkgdir/" --optimize=1
}

package_python2-cachey(){
  depends=('python2-heapdict')
  cd "$srcdir/$_pkgname-py2"
  install -D -m644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
  python2 setup.py install --root="$pkgdir/" --optimize=1
}

check(){
  cd "$srcdir/$_pkgname"
  nosetests
  cd "$srcdir/$_pkgname-py2"
  nosetests2
}
# vim:ts=2:sw=2:et:
