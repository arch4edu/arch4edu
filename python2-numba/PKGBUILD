# Maintainer: Michael Schubert <mschu.dev at gmail>
pkgname=python2-numba
pkgver=0.45.1
pkgrel=1
pkgdesc="NumPy aware dynamic Python compiler using LLVM"
url="http://numba.pydata.org/"
arch=('i686' 'x86_64')
license=('BSD')
depends=('python2-llvmlite>=0.28.0' 'python2-numpy>=1.10' 'python2-funcsigs'
         'python2-singledispatch')
makedepends=('cython2')
source=("https://github.com/numba/numba/archive/$pkgver.tar.gz")
sha256sums=('6a5da423d2f7aae9d84bb98166483d86e90146ab5cf15437506a5766cfae999e')

build() {
  cd "$srcdir/numba-$pkgver"
  python2 setup.py build
}

check_disabled() { # takes too much time/memory
  cd "$srcdir/numba-$pkgver"
  python2 setup.py test
}

package() {
  cd "$srcdir/numba-$pkgver"
  python2 setup.py install --skip-build --prefix=/usr --root="$pkgdir" --optimize=1

  mv "$pkgdir"/usr/bin/numba{,2}
  mv "$pkgdir"/usr/bin/pycc{,2}
}
