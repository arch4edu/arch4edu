# Maintainer: Michael Schubert <mschu.dev at gmail>
pkgname=python-numba
pkgver=0.40.0
pkgrel=1
pkgdesc="NumPy aware dynamic Python compiler using LLVM"
url="http://numba.pydata.org/"
arch=('i686' 'x86_64')
license=('BSD')
depends=('python-llvmlite' 'python-numpy')
makedepends=('cython')
source=("https://github.com/numba/numba/archive/$pkgver.tar.gz")
sha256sums=('a26f899a0fda9ca282f87587e0e9254d90b07b6ae8bc9a827ebcd6847a48c41b')

build() {
  cd "$srcdir/numba-$pkgver"
  python setup.py build
}

package() {
  cd "$srcdir/numba-$pkgver"
  python setup.py install --skip-build --prefix=/usr --root="$pkgdir" --optimize=1
}
