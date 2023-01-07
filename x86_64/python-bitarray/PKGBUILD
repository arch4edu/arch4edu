# Contributor: Pedro Martinez-Julia (pedromj@um.es)

pkgname=python-bitarray
pkgver=2.6.2
pkgrel=1
pkgdesc="Efficient arrays of booleans for Python"
arch=('i686' 'x86_64')
url="https://github.com/ilanschnell/bitarray"
license=('PSF')
depends=('python')
makedepends=('python-distribute' 'python-wheel' 'python-build' 'python-installer')
source=(https://files.pythonhosted.org/packages/source/b/bitarray/bitarray-$pkgver.tar.gz)
sha256sums=('90bac83ba6c37ab5048b43e07eba7d0de12f301ad6641633656fa269618a7301')

build() {
  cd "$srcdir"/bitarray-$pkgver
  python -m build --wheel --no-isolation
}

package() {
  cd "$srcdir"/bitarray-$pkgver
  python -m installer --destdir="$pkgdir" dist/*.whl
}
