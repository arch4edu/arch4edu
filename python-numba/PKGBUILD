# Maintainer: Michael Schubert <mschu.dev at gmail>
pkgname=python-numba
pkgver=0.49.0
pkgrel=1
pkgdesc="NumPy aware dynamic Python compiler using LLVM"
url="http://numba.pydata.org/"
arch=('i686' 'x86_64')
license=('BSD')
depends=('python-llvmlite>=0.32.0' 'python-numpy>=1.15')
makedepends=('cython')
optdepends=('python-scipy>=1.0.0')
source=("https://github.com/numba/numba/archive/$pkgver.tar.gz")
sha256sums=('8658d0f56817bedf1befcd07ca742023bd83a77ce3826aa37e0a4297f3ede330')

build() {
  cd "$srcdir/numba-$pkgver"
  python setup.py build
}

check_disabled() { #ERROR: unittest/loader.py returned decorator, not test
  cd "$srcdir/numba-$pkgver"
  python setup.py test
}

package() {
  cd "$srcdir/numba-$pkgver"
  python setup.py install --skip-build --prefix=/usr --root="$pkgdir" --optimize=1
}
