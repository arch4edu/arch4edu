# Maintainer: Michael Schubert <mschu.dev at gmail>
pkgname=python2-numba
pkgver=0.39.0
pkgrel=1
pkgdesc="NumPy aware dynamic Python compiler using LLVM"
url="http://numba.pydata.org/"
arch=('i686' 'x86_64')
license=('BSD')
depends=('python2-llvmlite' 'python2-numpy' 'python2-funcsigs')
makedepends=('cython2')
source=("https://github.com/numba/numba/archive/$pkgver.tar.gz")
sha256sums=('96811f814cafefc05999467ec28522789cb8381448e240ae212ebd3021d03c2b')

build() {
  cd "$srcdir/numba-$pkgver"
  python2 setup.py build
}

package() {
  cd "$srcdir/numba-$pkgver"
  python2 setup.py install --skip-build --prefix=/usr --root="$pkgdir" --optimize=1

  mv "$pkgdir"/usr/bin/numba{,2}
  mv "$pkgdir"/usr/bin/pycc{,2}
}
