# Maintainer: Heptazhou <zhou at 0h7z dot com>

pkgbase_=x11iraf
pkgname_=xgterm
pkgname=$pkgname_-bin
debver=2.2+dfsg-1
pkgver=2.2
pkgrel=1
pkgdesc="Terminal emulator to work with IRAF"
arch=("x86_64")
url="https://github.com/iraf-community/$pkgbase_"
url_="https://deb.debian.org/debian/pool/main/${pkgbase_:0:1}/$pkgbase_"
license=("custom")
options=(!debug)
provides=("$pkgname_")
conflicts=("$pkgname_")
depends=("libxaw" "ncurses" "tcl" "xaw3d")
optdepends=("iraf: Image Reduction and Analysis Facility")
source=(${url_}/${pkgname_}_${debver}_amd64.deb)
sha256sums=("0ffa32e75324a317e783738aa466ecc5612e13dd886008fa28efe39520a01879")
# https://tracker.debian.org/pkg/x11iraf

package() {
	cd -- "$srcdir/"
	tar fx "data.tar.xz"

	mkdir "usr/share/licenses/$pkgname_/" -p
	mv -T "usr/share"/{"doc/$pkgname_/copyright","licenses/$pkgname_/LICENSE"}
	rm -r "usr/share"/{"doc","lintian"} -f
	cp -t "$pkgdir/" -a "usr"

	mkdir "$pkgdir/usr/lib/" -p
	ln -s "$pkgdir/usr/lib/libXaw3d.so"{,.6} -r
}
