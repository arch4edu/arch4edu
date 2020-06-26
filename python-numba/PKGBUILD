# Maintainer: Michael Schubert <mschu.dev at gmail>
pkgname=python-numba
pkgver=0.50.1
pkgrel=1
pkgdesc="NumPy aware dynamic Python compiler using LLVM"
url="http://numba.pydata.org/"
arch=('i686' 'x86_64')
license=('BSD')
depends=('python-llvmlite>=0.33.0' 'python-llvmlite<0.34' 'python-numpy>=1.15')
makedepends=('cython')
optdepends=('python-scipy>=1.0.0')
source=(numba-$pkgver.tar.gz::"https://github.com/numba/numba/archive/$pkgver.tar.gz")
sha256sums=('f45d6a85c8aedde8c99e775070f3fa699d6b941f0f635e268c14b3561d787789')

build() {
  cd "$srcdir/numba-$pkgver"
  python setup.py build
}

check_disabled() { #ERROR: TypeError None is not callable
  cd "$srcdir/numba-$pkgver"
  python setup.py test
}

package() {
  cd "$srcdir/numba-$pkgver"
  python setup.py install --skip-build --prefix=/usr --root="$pkgdir" --optimize=1
}
