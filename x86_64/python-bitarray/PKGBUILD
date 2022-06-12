# Contributor: Pedro Martinez-Julia (pedromj@um.es)

pkgname=python-bitarray
pkgver=2.5.1
pkgrel=1
pkgdesc="Efficient arrays of booleans for Python"
arch=('i686' 'x86_64')
url="https://github.com/ilanschnell/bitarray"
license=('PSF')
depends=('python')
makedepends=('python-distribute')
source=(https://files.pythonhosted.org/packages/source/b/bitarray/bitarray-$pkgver.tar.gz)
sha256sums=('8d38f60751008099a659d5acfb35ef4150183effd5b2bfa6c10199270ddf4c9c')

package() {
  cd "$srcdir"/bitarray-$pkgver
  python setup.py install --root="$pkgdir" -O1
}
