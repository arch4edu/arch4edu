# Maintainer: Sven Lechner <sven[dot]lechner[at]rwth-aachen[dot]de>

pkgname=act
pkgver=0.2.19
pkgrel=1
pkgdesc='Run your GitHub Actions locally'
arch=('x86_64')
url='https://github.com/nektos/act'
license=('MIT')
provides=('act')
conflicts=('act')
depends=('docker')
source=("$pkgname-$pkgver.src.tar.gz::https://github.com/nektos/act/releases/download/v$pkgver/act_Linux_x86_64.tar.gz")
sha256sums=('be52d1cb8cc5d2f9313ed1001807911ba3fed7a8201b96cc930ddd0ebef21dff')

package() {
    # Install binary.
    install -Dm755 "$srcdir/act" "$pkgdir/usr/bin/act"

    # Install license.
    install -Dm644 "$srcdir/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
