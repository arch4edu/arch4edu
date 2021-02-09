# Maintainer: Michael Schubert <mschu.dev at gmail>
pkgname=python-llvmlite
pkgver=0.36.0rc1
pkgrel=1
pkgdesc="Lightweight LLVM python binding for writing JIT compilers"
url="https://github.com/numba/llvmlite"
arch=('i686' 'x86_64')
license=('BSD')
depends=('python' 'llvm10-libs>=10.0.0' 'llvm10-libs<10.1.0')
makedepends=('cython' 'llvm10>=10.0.0' 'llvm10<10.1.0')
source=(llvmlite-$pkgver.tar.gz::"https://github.com/numba/llvmlite/archive/v$pkgver.tar.gz")
sha256sums=('dd1cbb6471169cf7af41da20b1f07b0eaaef75664bd655ff317bbd0c8ee0499b')

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
