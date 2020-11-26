# Maintainer: Sven Lechner <sven[dot]lechner[at]rwth-aachen[dot]de>

pkgname=act
pkgver=0.2.17
pkgrel=1
pkgdesc='Run your GitHub Actions locally'
arch=('x86_64')
url='https://github.com/nektos/act'
license=('MIT')
provides=('act')
conflicts=('act')
depends=('docker')
source=("$pkgname-$pkgver.src.tar.gz::https://github.com/nektos/act/releases/download/v$pkgver/act_Linux_x86_64.tar.gz")
sha256sums=('84456c6350b4a153311aa2d8c5887ad77ef8820d3ac2ce2b6480f282e8551279')

package() {
    # Install binary.
    install -Dm755 "$srcdir/act" "$pkgdir/usr/bin/act"

    # Install license.
    install -Dm644 "$srcdir/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
