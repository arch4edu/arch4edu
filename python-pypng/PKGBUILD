# Maintainer: Massimiliano Torromeo <massimiliano.torromeo@gmail.com>

pkgname=python-pypng
pkgver=0.0.20
pkgrel=1
pkgdesc="Pure Python library for PNG image encoding/decoding"
arch=(any)
url="https://github.com/drj11/pypng"
license=('MIT')
depends=('python')
source=("$url/archive/pypng-$pkgver.tar.gz")

build() {
    cd "$srcdir"/pypng-pypng-$pkgver
    python setup.py build
}

package() {
    cd "$srcdir"/pypng-pypng-$pkgver
    python setup.py install -O1 --skip-build --root="$pkgdir"
}

sha256sums=('d008a1f1f79633937ed2aa1742c7c077359edce53764b8b247891056ddca913c')
