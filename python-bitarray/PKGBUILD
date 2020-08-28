# Contributor: Pedro Martinez-Julia (pedromj@um.es)

pkgname=python-bitarray
pkgver=1.5.3
pkgrel=1
pkgdesc="Efficient arrays of booleans for Python"
arch=('i686' 'x86_64')
url="https://github.com/ilanschnell/bitarray"
license=('PSF')
depends=('python')
makedepends=('python-distribute')
source=(https://files.pythonhosted.org/packages/source/b/bitarray/bitarray-$pkgver.tar.gz)
sha256sums=('567631fc922b1c2c528c376795f18dcc0604d18702e0b8b50e8e35f0474214a5')

package() {
  cd "$srcdir"/bitarray-$pkgver
  python setup.py install --root="$pkgdir" -O1
}
