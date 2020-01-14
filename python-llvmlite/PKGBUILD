# Maintainer: Michael Schubert <mschu.dev at gmail>
pkgname=python-llvmlite
pkgver=0.31.0
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
sha256sums=('a2c431ce2240cda8d4a7b6cce84ac012e0385f5b62ef9911249b000c7ef2c558')

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
