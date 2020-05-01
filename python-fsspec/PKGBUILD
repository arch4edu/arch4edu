# Maintainer: Guillaume Horel <guillaume.horel@gmail.com>

pkgname=python-fsspec
_pkgname=filesystem_spec
pkgver=0.7.3
pkgrel=1
pkgdesc="A specification that python filesystems should adhere to."
arch=('any')
url="https://github.com/intake/filesystem_spec"
license=('BSD')
depends=('python')
checkdepends=('docker' 'python-paramiko' 'python-pyftpdlib' 'python-pytest')
optdepends=()
makedepends=('python-setuptools')
source=("$pkgname-$pkgver.tar.gz::https://github.com/intake/filesystem_spec/archive/$pkgver.tar.gz")
sha256sums=('3f4d60a4ff89134908016809de75ff0b82096df5f41af5f97b1508fd6d9d7d49')

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
