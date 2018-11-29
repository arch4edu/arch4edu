# Maintainer: Michael Schubert <mschu.dev at gmail>
pkgname=python-numba
pkgver=0.41.0
pkgrel=1
pkgdesc="NumPy aware dynamic Python compiler using LLVM"
url="http://numba.pydata.org/"
arch=('i686' 'x86_64')
license=('BSD')
depends=('python-llvmlite' 'python-numpy')
makedepends=('cython')
source=("https://github.com/numba/numba/archive/$pkgver.tar.gz")
sha256sums=('3d5725a2719d45e736d5acfbee63c9e7d5fab3b6406f59257fea6d10dbf5f416')

build() {
  cd "$srcdir/numba-$pkgver"
  python setup.py build
}

package() {
  cd "$srcdir/numba-$pkgver"
  python setup.py install --skip-build --prefix=/usr --root="$pkgdir" --optimize=1
}
