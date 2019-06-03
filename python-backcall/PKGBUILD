# Maintainer: asm0dey <pavel.finkelshtein+AUR@gmail.com>

pkgname=python-backcall
pkgver=0.1
pkgrel=1
pkgdesc="Backwards compatible callback APIs"
url="https://github.com/takluyver/backcall"
arch=(any)
license=('BSD')
depends=(
    'python'
)
makedepends=('python-setuptools')
source=(
    "https://github.com/takluyver/backcall/archive/$pkgver.zip"
    "https://raw.githubusercontent.com/takluyver/backcall/master/LICENSE"
)
md5sums=('ba32936cb9db843da2336ef55c9c0dd1' '40e56b724d016484a7f790ec826d3ffc')


build() {
    cd "$srcdir/backcall-$pkgver"
    python setup.py build
}

package() {
    cd "$srcdir/backcall-$pkgver"
    python setup.py install --skip-build --root="$pkgdir" --optimize=1
    install -D --mode 644 --target-directory "$pkgdir/usr/share/licenses/$pkgname" "$srcdir/LICENSE"
}

