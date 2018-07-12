# Maintainer: Massimiliano Torromeo <massimiliano.torromeo@gmail.com>

pkgname=python-mysqlclient
_libname=${pkgname/python-/}
pkgver=1.3.13
pkgrel=1
pkgdesc="Fork of MySQL-python with support for Python 3"
arch=('i686' 'x86_64' 'armv7h')
url="https://github.com/PyMySQL/mysqlclient-python"
license=('GPL')
depends=('python' 'libmariadbclient')
makedepends=('mariadb' 'python-setuptools')
source=("https://files.pythonhosted.org/packages/source/${_libname:0:1}/$_libname/$_libname-$pkgver.tar.gz")

build() {
    cd "$srcdir"/$_libname-$pkgver
    python setup.py build
}

package() {
    cd "$srcdir"/$_libname-$pkgver
    python setup.py install -O1 --skip-build --root="$pkgdir"
}

sha256sums=('ff8ee1be84215e6c30a746b728c41eb0701a46ca76e343af445b35ce6250644f')
