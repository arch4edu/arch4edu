# Maintainer: piernov <piernov@piernov.org>

pkgname=python-jsonref
pkgver=1.1.0
pkgrel=1
pkgdesc="An implementation of JSON Reference for Python"
arch=('x86_64')
url="https://pypi.org/project/jsonref"
license=('MIT')
depends=('python')
makedepends=('python-pdm-pep517' 'python-build' 'python-installer')
source=("https://files.pythonhosted.org/packages/aa/0d/c1f3277e90ccdb50d33ed5ba1ec5b3f0a242ed8c1b1a85d3afeb68464dca/jsonref-$pkgver.tar.gz")
md5sums=('c6bb6e762afc840dbb246fbcfeea6800')

build() {
  cd "$srcdir"/jsonref-$pkgver
  python -m build --wheel --no-isolation
}

package() {
  cd "$srcdir"/jsonref-$pkgver
  python -m installer --destdir="$pkgdir" dist/*.whl
}
