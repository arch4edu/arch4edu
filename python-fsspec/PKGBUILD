# Maintainer: Guillaume Horel <guillaume.horel@gmail.com>

pkgname=python-fsspec
_pkgname=filesystem_spec
pkgver=0.6.2
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
sha256sums=('874c635ded9ca22d2284fc6970531d05d17ece796e3f81b5740b6704bd09578b')

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
