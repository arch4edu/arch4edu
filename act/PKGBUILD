# Maintainer: Sven Lechner <sven[dot]lechner[at]rwth-aachen[dot]de>

pkgname=act
pkgver=0.2.6
pkgrel=1
pkgdesc='Run your GitHub Actions locally'
arch=('x86_64')
url='https://github.com/nektos/act'
license=('MIT')
provides=('act')
conflicts=('act')
source=("$pkgname-$pkgver.src.tar.gz::https://github.com/nektos/act/releases/download/v$pkgver/act_Linux_x86_64.tar.gz")
sha256sums=('92d0ed1b1611fc43ed1c8785e963b09f585c12703ec535d192b63c84cb452273')

package() {
    # Install binary.
    install -Dm755 "$srcdir/act" "$pkgdir/usr/bin/act"

    # Install license.
    install -Dm644 "$srcdir/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
