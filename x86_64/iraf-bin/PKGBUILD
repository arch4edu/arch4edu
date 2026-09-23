# Maintainer: Heptazhou <zhou at 0h7z dot com>

pkgbase_=iraf
pkgname_=($pkgbase_{,-noao})
pkgname=(${pkgname_[@]/%/-bin})
debver=2.18.2-4
pkgver=2.18.2
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
	"fd253133de6a1107683494eedcb8d69447e122a59b72e46115146474e4bc9426"
	"950d9c79375558a0d4ca16179b48da9ad447dbffaa791097c3a2358889b8c5f7"
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
