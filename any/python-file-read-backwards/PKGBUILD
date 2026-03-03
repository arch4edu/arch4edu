# Maintainer: Benoît Allard <benoit.allard@gnx.de>
pkgname=python-file-read-backwards
pkgver=3.2.0
pkgrel=1
pkgdesc="Memory efficient way of reading files line-by-line from the end of file"
arch=('any')
url="https://github.com/RobinNil/file_read_backwards"
license=('MIT')
makedepends=('python-build' 'python-installer' 'python-setuptools' 'python-wheel')
depends=("python")
_name=${pkgname#python-}
source=("$pkgname-$pkgver.tar.gz::https://github.com/RobinNil/${_name//-/_}/archive/v$pkgver.tar.gz")
sha256sums=('ee4c2915a5aaceaf3e5791226109c39f7324da99bd4b8466cbec5504ed126699')

build() {
    cd ${_name//-/_}-$pkgver
    python -m build --wheel --no-isolation
}

package() {
    cd ${_name//-/_}-$pkgver
    python -m installer --destdir="$pkgdir" dist/*.whl
}
