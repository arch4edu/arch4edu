# Maintainer: Michael Schubert <mschu.dev at gmail>
pkgname=python2-llvmlite
pkgver=0.28.0
pkgrel=2
pkgdesc="Lightweight LLVM python binding for writing JIT compilers"
url="https://github.com/numba/llvmlite"
arch=('i686' 'x86_64')
license=('BSD')
depends=('python2-enum34' 'llvm7-libs')
makedepends=('cython2' 'llvm7<7.1.0' )
source=("https://github.com/numba/llvmlite/archive/v$pkgver.tar.gz")
sha256sums=('39868fd2d86cb724ceaac4a34773e47e3b3ba6eeb445b9ac0abaf17a620e74dc')

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
