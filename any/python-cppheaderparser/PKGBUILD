# Maintainer: Manuel Schmitzberger <ms@ms-sw.at>

pkgname=python-cppheaderparser
_name=CppHeaderParser
pkgver=2.7.4
pkgrel=4
pkgdesc="Parse C++ header files and generate a data structure representing the class"
arch=('any')
url="http://senexcanis.com/open-source/cppheaderparser"
license=('BSD')
depends=('python-ply')
makedepends=('python-setuptools')
source=("https://pypi.org/packages/source/${_name:0:1}/$_name/$_name-$pkgver.tar.gz")
sha256sums=('382b30416d95b0a5e8502b214810dcac2a56432917e2651447d3abe253e3cc42')

build() {
  cd "$_name-$pkgver"
  python setup.py build
}

package() {
  cd "$_name-$pkgver"
  python setup.py install --root="$pkgdir" --optimize=1 --skip-build
}
