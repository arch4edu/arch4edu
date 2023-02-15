# Contributor: Pedro Martinez-Julia (pedromj@um.es)

pkgname=python-bitarray
pkgver=2.7.2
pkgrel=1
pkgdesc="Efficient arrays of booleans for Python"
arch=('i686' 'x86_64')
url="https://github.com/ilanschnell/bitarray"
license=('PSF')
depends=('python')
makedepends=('python-distribute' 'python-wheel' 'python-build' 'python-installer')
source=(https://files.pythonhosted.org/packages/source/b/bitarray/bitarray-$pkgver.tar.gz)
sha256sums=('7ea42120162bc089a169c58039ce2f0198b5d9bb6cac7c076c3035176335811c')

build() {
  cd "$srcdir"/bitarray-$pkgver
  python -m build --wheel --no-isolation
}

package() {
  cd "$srcdir"/bitarray-$pkgver
  python -m installer --destdir="$pkgdir" dist/*.whl
}
