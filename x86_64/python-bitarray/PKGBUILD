# Contributor: Pedro Martinez-Julia (pedromj@um.es)

pkgname=python-bitarray
pkgver=2.8.4
pkgrel=1
pkgdesc="Efficient arrays of booleans for Python"
arch=('i686' 'x86_64')
url="https://github.com/ilanschnell/bitarray"
license=('PSF')
depends=('python')
makedepends=('python-distribute' 'python-wheel' 'python-build' 'python-installer')
source=(https://files.pythonhosted.org/packages/source/b/bitarray/bitarray-$pkgver.tar.gz)
sha256sums=('2c0ba71445ee0932e510f1b0248f53b7a52926f1f78c93b868fcbe6536e61a1d')

build() {
  cd "$srcdir"/bitarray-$pkgver
  python -m build --wheel --no-isolation
}

package() {
  cd "$srcdir"/bitarray-$pkgver
  python -m installer --destdir="$pkgdir" dist/*.whl
}
