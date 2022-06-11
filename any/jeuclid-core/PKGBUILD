# Maintainer: Alucryd <alucryd at gmail dot com>
# Maintainer: Stefan Husmann <stefan-husmann at t-online dot de>
# Contributor: Simon Lipp <sloonz+aur at gmail dot com>

pkgname=jeuclid-core
pkgver=3.1.9
pkgrel=1
pkgdesc="MathML renderer for Java"
arch=('any')
url="http://jeuclid.sourceforge.net/"
license=(APACHE)
depends=('java-runtime')
source=("https://downloads.sourceforge.net/jeuclid/jeuclid-minimal-$pkgver-distribution.zip")
md5sums=('c89067cdb005008f2ad46d579ed2086b')
sha1sums=('69d11a92a48569aec648317b3cb175c3db72a2d1')
sha256sums=('35df0ce04b2fdb527feba9122bc305fe3cd26b5d5b89e2148359833a84cbfbe3')
sha512sums=('8d2c423d7444d19f6c0f2733e0ac32206487f9c817c789cba36a7dfaa0bbdc459efb8b562423b9ad9efd2980586e8f6812685ac27183132d273c7fcaaea22a5b')

package() {
    install -Dm644 $srcdir/jeuclid-minimal-$pkgver/repo/$pkgname-$pkgver.jar $pkgdir/usr/share/java/jeuclid/$pkgname.jar
}
