# Maintainer: Heptazhou <zhou at 0h7z dot com>

pkgbase_=iraf
pkgname_=($pkgbase_{,-noao})
pkgname=(${pkgname_[@]/%/-bin})
debver=2.18.1-2
pkgver=2.18.1
pkgrel=1
pkgdesc="IRAF - Image Reduction and Analysis Facility"
arch=("x86_64")
url="https://github.com/iraf-community/$pkgbase_"
url_="https://deb.debian.org/debian/pool/main/${pkgbase_:0:1}/$pkgbase_"
license=("custom")
options=(!debug)
noextract=(${pkgname_[@]/%/_${debver}_amd64.deb})
source=(${noextract[@]/#/${url_}/})
sha256sums=(
	"d6dec66efc57b6e5cf8086685efc18a95a0ec4936d5219e2c867c6c3a7de4e99"
	"487d687a1e958b3c9abd4f4b6c180e6c1a7a22f85817013d011dd44381a50cdb"
)
# https://tracker.debian.org/pkg/iraf

prepare() {
	for name in "${pkgname_[@]}"; do
		ar x "${name}_${debver}_amd64.deb" "data.tar.xz"
		mkdir "$name/" -p
		tar Cfx "$name" "data.tar.xz" && rm "data.tar.xz"
	done
}

package_iraf-bin() {
	provides=("$pkgbase_")
	conflicts=("$pkgbase_")
	depends=("glibc" "readline" "sh")
	optdepends=(
		"$pkgbase_-noao: IRAF NOAO data reduction package"
		"ds9: Image display tool for astronomy"
		"xgterm: Terminal emulator to work with IRAF"
	)

	cd -- "$srcdir/$pkgbase_/"

	mkdir "usr/share/licenses/$pkgbase_/" -p
	mv -T "usr/share"/{"doc/$pkgbase_/copyright","licenses/$pkgbase_/LICENSE"}
	rm -r "usr/share"/{"doc","lintian"} -f
	cp -t "$pkgdir/" -a "usr" "etc"
}

package_iraf-noao-bin() {
	provides=("$pkgbase_-noao")
	conflicts=("$pkgbase_-noao")
	depends=("$pkgbase_")

	cd -- "$srcdir/$pkgbase_-noao/"

	mkdir "usr/share/licenses/" -p
	ln -s "usr/share/licenses/$pkgbase_"{,-noao} -r
	rm -r "usr/share"/{"doc","lintian"} -f
	cp -t "$pkgdir/" -a "usr"
}
