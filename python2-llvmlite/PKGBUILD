# Maintainer: Michael Schubert <mschu.dev at gmail>
pkgname=python2-llvmlite
pkgver=0.30.0
pkgrel=3
pkgdesc="Lightweight LLVM python binding for writing JIT compilers"
url="https://github.com/numba/llvmlite"
arch=('i686' 'x86_64')
license=('BSD')
#depends=('python2-enum34' 'llvm-libs>=7.0.0' 'llvm-libs<9.1.0')
#makedepends=('cython2' 'llvm>=7.0.0' 'llvm<9.1.0' )
depends=('python2-enum34' 'llvm7-libs')
makedepends=('cython2' 'llvm7')
source=("https://github.com/numba/llvmlite/archive/v$pkgver.tar.gz")
sha256sums=('07b72dfdd8e6e5bc718fc7cd00517b94bf00caf29b387605adb0779c5c63dc28')

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
