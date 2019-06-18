# Maintainer: Michael Schubert <mschu.dev at gmail>
pkgname=python2-numba
pkgver=0.44.1
pkgrel=1
pkgdesc="NumPy aware dynamic Python compiler using LLVM"
url="http://numba.pydata.org/"
arch=('i686' 'x86_64')
license=('BSD')
depends=('python2-llvmlite>=0.28.0' 'python2-numpy>=1.10' 'python2-funcsigs'
         'python2-singledispatch')
makedepends=('cython2')
source=("https://github.com/numba/numba/archive/$pkgver.tar.gz")
sha256sums=('0f6bae0253030f486a9fc43c21fb43c3fe9552323220438c35633f8061d6a44b')

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
