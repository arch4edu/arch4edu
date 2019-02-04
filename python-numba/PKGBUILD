# Maintainer: Michael Schubert <mschu.dev at gmail>
pkgname=python-numba
pkgver=0.42.1
pkgrel=1
pkgdesc="NumPy aware dynamic Python compiler using LLVM"
url="http://numba.pydata.org/"
arch=('i686' 'x86_64')
license=('BSD')
depends=('python-llvmlite' 'python-numpy')
makedepends=('cython')
source=("https://github.com/numba/numba/archive/$pkgver.tar.gz")
sha256sums=('e6cc895d40e4b8e034acadce775d99c9ad8972f349ee8890b0a77ff183af52a9')

build() {
  cd "$srcdir/numba-$pkgver"
  python setup.py build
}

package() {
  cd "$srcdir/numba-$pkgver"
  python setup.py install --skip-build --prefix=/usr --root="$pkgdir" --optimize=1
}
