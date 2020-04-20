# Contributor: Pedro Martinez-Julia (pedromj@um.es)

pkgname=python-bitarray
pkgver=1.2.1
pkgrel=1
pkgdesc="Efficient arrays of booleans for Python"
arch=('i686' 'x86_64')
url="https://github.com/ilanschnell/bitarray"
license=('PSF')
depends=('python')
makedepends=('python-distribute')
source=(https://files.pythonhosted.org/packages/source/b/bitarray/bitarray-$pkgver.tar.gz)
sha256sums=('2ed675f460bb0d3d66fd8042a6f1f0d36cf213e52e72a745283ddb245da7b9cf')

package() {
  cd "$srcdir"/bitarray-$pkgver
  python setup.py install --root="$pkgdir" -O1
}
