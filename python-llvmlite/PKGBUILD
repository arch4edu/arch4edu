# Maintainer: Michael Schubert <mschu.dev at gmail>
pkgname=python-llvmlite
pkgver=0.27.0
pkgrel=3
pkgdesc="Lightweight LLVM python binding for writing JIT compilers"
url="https://github.com/numba/llvmlite"
arch=('i686' 'x86_64')
license=('BSD')
depends=('python' 'llvm>=7.0.0' 'llvm<7.1.0' 'llvm-libs')
makedepends=('cython')
source=("https://github.com/numba/llvmlite/archive/v$pkgver.tar.gz")
sha256sums=('0469c683cfadb0484fb1a1f89a3df537864e9f2ad89df927c4349d90242dedca')

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
