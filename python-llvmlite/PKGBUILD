# Maintainer: Michael Schubert <mschu.dev at gmail>
pkgname=python-llvmlite
pkgver=0.32.0
pkgrel=1
pkgdesc="Lightweight LLVM python binding for writing JIT compilers"
url="https://github.com/numba/llvmlite"
arch=('i686' 'x86_64')
license=('BSD')
#depends=('python' 'llvm-libs>=7.0.0' 'llvm-libs<9.1.0')
#makedepends=('cython' 'llvm>=7.0.0' 'llvm<9.1.0')
depends=('python' 'llvm8-libs')
makedepends=('cython' 'llvm8')
source=("https://github.com/numba/llvmlite/archive/v$pkgver.tar.gz")
sha256sums=('15d71df80e8dfc3ff50c60d55db3396be4232db2a47c8f53ee47e48faf1953c7')

build() {
  cd "$srcdir/llvmlite-$pkgver"
  python setup.py build
}

check() {
  cd "$srcdir/llvmlite-$pkgver"
  python setup.py check
}

package() {
  cd "$srcdir/llvmlite-$pkgver"
  python setup.py install --skip-build --prefix=/usr --root="$pkgdir" --optimize=1

  pydir=$(python -c "from distutils.sysconfig import get_python_lib; \
    print(get_python_lib())")
  install -m755 "$srcdir"/llvmlite-$pkgver/ffi/libllvmlite.so \
    "$pkgdir/$pydir"/llvmlite/binding
}
