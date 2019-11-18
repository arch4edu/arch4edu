# Maintainer: Guillaume Horel <guillaume.horel@gmail.com>

pkgname=python-fsspec
_pkgname=filesystem_spec
pkgver=0.6.0
pkgrel=1
pkgdesc="A specification that python filesystems should adhere to."
arch=('any')
url="https://github.com/intake/filesystem_spec"
license=('BSD')
depends=('python')
checkdepends=('docker' 'python-dask' 'python-pyftpdlib' 'python-pytest')
optdepends=()
makedepends=('python-setuptools')
source=("$pkgname-$pkgver.tar.gz::https://github.com/intake/filesystem_spec/archive/$pkgver.tar.gz")
sha256sums=('9053a8bfd5d49ca3d1a2104c20553ac5c406a1942d6b352f5588372adb2c7568')

package(){
  cd "$srcdir/$_pkgname-$pkgver"
  install -D -m644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
  python setup.py install --root="$pkgdir/" --optimize=1
}

check(){
  cd "$srcdir/$_pkgname-$pkgver"
  py.test
}
# vim:ts=2:sw=2:et:
