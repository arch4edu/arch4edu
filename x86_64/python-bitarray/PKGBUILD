# Contributor: Pedro Martinez-Julia (pedromj@um.es)

pkgname=python-bitarray
pkgver=2.8.5
pkgrel=1
pkgdesc="Efficient arrays of booleans for Python"
arch=('i686' 'x86_64')
url="https://github.com/ilanschnell/bitarray"
license=('PSF')
depends=('python')
makedepends=('python-distribute' 'python-wheel' 'python-build' 'python-installer')
source=(https://files.pythonhosted.org/packages/source/b/bitarray/bitarray-$pkgver.tar.gz)
sha256sums=('b7564fd218cc4479f7f0106d341e096f78907b47865aeeff702c807df1927c01')

build() {
  cd "$srcdir"/bitarray-$pkgver
  python -m build --wheel --no-isolation
}

package() {
  cd "$srcdir"/bitarray-$pkgver
  python -m installer --destdir="$pkgdir" dist/*.whl
}
