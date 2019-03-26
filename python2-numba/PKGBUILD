# Maintainer: Michael Schubert <mschu.dev at gmail>
pkgname=python2-numba
pkgver=0.43.0
pkgrel=2
pkgdesc="NumPy aware dynamic Python compiler using LLVM"
url="http://numba.pydata.org/"
arch=('i686' 'x86_64')
license=('BSD')
depends=('python2-llvmlite>=0.28.0' 'python2-numpy>=1.10' 'python2-funcsigs')
makedepends=('cython2')
checkdepends=('python2-singledispatch')
source=("https://github.com/numba/numba/archive/$pkgver.tar.gz")
sha256sums=('037d2fd46318e94b7dd33deed0284f2a59571ba0439ec1f1e1394b7c9aee00f2')

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
