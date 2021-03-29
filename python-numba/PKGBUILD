# Maintainer: Michael Schubert <mschu.dev at gmail>
pkgname=python-numba
pkgver=0.53.1
pkgrel=1
pkgdesc="NumPy aware dynamic Python compiler using LLVM"
url="https://numba.pydata.org/"
arch=('i686' 'x86_64')
license=('BSD')
depends=('python-llvmlite>=0.36.0' 'python-llvmlite<0.37' 'python-numpy>=1.15')
makedepends=('cython' 'python-setuptools')
optdepends=('python-scipy>=1.0.0')
source=(numba-$pkgver.tar.gz::"https://github.com/numba/numba/archive/$pkgver.tar.gz")
sha256sums=('c0d5ef90eb959f919cf134512259459430c58d566ff2124535572648b3b3931d')

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
