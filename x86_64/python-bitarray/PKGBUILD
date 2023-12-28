# Contributor: Pedro Martinez-Julia (pedromj@um.es)

pkgname=python-bitarray
pkgver=2.9.1
pkgrel=1
pkgdesc="Efficient arrays of booleans for Python"
arch=('i686' 'x86_64')
url="https://github.com/ilanschnell/bitarray"
license=('PSF')
depends=('python')
makedepends=('python-distribute' 'python-wheel' 'python-build' 'python-installer')
source=(https://files.pythonhosted.org/packages/source/b/bitarray/bitarray-$pkgver.tar.gz)
sha256sums=('912efbeed6d8b155c8e8c37464f79d75b1de58936c0f29ffb599ce95af5563f2')

build() {
  cd "$srcdir"/bitarray-$pkgver
  python -m build --wheel --no-isolation
}

package() {
  cd "$srcdir"/bitarray-$pkgver
  python -m installer --destdir="$pkgdir" dist/*.whl
}
