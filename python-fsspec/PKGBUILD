# Maintainer: Guillaume Horel <guillaume.horel@gmail.com>

pkgname=python-fsspec
_pkgname=filesystem_spec
pkgver=0.4.1
pkgrel=1
pkgdesc="A specification that python filesystems should adhere to."
arch=('any')
url="https://github.com/iintake/filesystem_spec"
license=('BSD')
depends=('python')
checkdepends=('docker' 'python-dask' 'python-pytest')
optdepends=()
makedepends=('python-setuptools')
source=("https://github.com/intake/filesystem_spec/archive/$pkgver.tar.gz")
sha256sums=('ed296f9c28e5546389739eef546eb1c70bac914f5c32baf0d616e1c574f6b0df')

package(){
  cd "$srcdir/$_pkgname-$pkgver"
  install -D -m644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
  python setup.py install --root="$pkgdir/" --optimize=1
}

#check(){
#  cd "$srcdir/$_pkgname-$pkgver"
#  py.test
#}
# vim:ts=2:sw=2:et:
