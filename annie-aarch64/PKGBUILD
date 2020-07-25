# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
# Contributor: Aniket Pradhan <aniket17133@iiitd.ac.in>
# Owner/Cofntributer: Xinzhao Xu <z2d@jifangcheng.com>

pkgname=annie
pkgver=0.9.6
pkgrel=3
arch=('x86_64' 'i686')
pkgdesc="A fast, simple and clean video downloader written in Go"
url="https://github.com/iawia002/annie"
license=("MIT")
makedepends=('git' 'dep')
depends=('go-pie' 'ffmpeg')
conflicts=("annie")
options=('!strip' '!emptydirs')
source=("annie::git+https://github.com/iawia002/annie#tag=${pkgver}")

prepare(){
	mkdir -p gopath/src/github.com
	ln -rTsf $pkgname $srcdir/gopath/src/github.com/$pkgname
	export GOPATH="$srcdir"/gopath
	cd $GOPATH/src/github.com/$pkgname
	dep init
	#dep ensure
}

build(){
	export GOPATH=$srcdir/gopath
	cd gopath/src/github.com/$pkgname
	go install \
		-gcflags "all=-trimpath=$GOPATH" \
		-asmflags "all=-trimpath=$GOPATH" \
		-ldflags "-extldflags $LDFLAGS" \
		-v ./...
}

package() {
	install -Dm755 gopath/bin/$pkgname "$pkgdir"/usr/bin/$pkgname

	for f in LICENSE COPYING LICENSE.* COPYING.*; do
		if [ -e "$srcdir/src/$_gourl/$f" ]; then
		install -Dm644 "$srcdir/src/$_gourl/$f" \
		"$pkgdir/usr/share/licenses/$pkgname/$f"
	fi
	done
}
md5sums=('SKIP')
