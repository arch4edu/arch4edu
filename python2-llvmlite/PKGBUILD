# Maintainer: Michael Schubert <mschu.dev at gmail>
pkgname=python2-llvmlite
pkgver=0.27.1
pkgrel=1
pkgdesc="Lightweight LLVM python binding for writing JIT compilers"
url="https://github.com/numba/llvmlite"
arch=('i686' 'x86_64')
license=('BSD')
depends=('python2-enum34' 'llvm>=7.0.0' 'llvm<7.1.0' 'llvm-libs')
makedepends=('cython2')
source=("https://github.com/numba/llvmlite/archive/v$pkgver.tar.gz")
sha256sums=('ef222a5b14d883fe7cc7ff23a03c2c2d2f3312f3505eed71cf9d4feea6adf16d')

build() {
  cd "$srcdir/llvmlite-$pkgver"
  python2 setup.py build
}

check() {
  cd "$srcdir/llvmlite-$pkgver"
  python2 setup.py check
}

package() {
  cd "$srcdir/llvmlite-$pkgver"
  python2 setup.py install --skip-build --prefix=/usr --root="$pkgdir" --optimize=1

  pydir=$(python2 -c "from distutils.sysconfig import get_python_lib; \
    print get_python_lib()")
  install -m755 "$srcdir"/llvmlite-$pkgver/ffi/libllvmlite.so \
    "$pkgdir/$pydir"/llvmlite/binding
}
