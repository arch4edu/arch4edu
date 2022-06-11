# Maintainer: Jingbei Li <i@jingbei.lli>
_pkgname='kaldi'
_gitname='irstlm'
pkgname="$_pkgname-$_gitname"
pkgdesc='Speech recognition research toolkit'
pkgver=r94.c358d7b
pkgrel=2
depends=('kaldi')
makedepends=('git')
arch=('x86_64' 'i686')
url='https://github.com/kaldi-asr/kaldi'
license=('APACHE')
source=("git+https://github.com/irstlm-team/irstlm"
	"https://github.com/kaldi-asr/kaldi/archive/master.zip"
	"install_irstlm.patch"
	)
sha256sums=('SKIP' 'SKIP' 'f23734f32d89c7529879e5f48519c8687b384281de261d17cfa59166ec56c6e1')

pkgver () {
	cd "${_gitname}"
	(
		set -o pipefail
		printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
	)
}

build () {
	cd $srcdir/$_pkgname-master/tools
	rm -rf $_gitname
	git clone $srcdir/$_gitname
	patch -p2 < $srcdir/install_irstlm.patch
	extras/install_irstlm.sh
}

package () {
	mkdir -p $pkgdir/opt/$_pkgname/tools/$_gitname
	cp -r $srcdir/$_pkgname-master/tools/$_gitname/{bin,include,lib} $pkgdir/opt/$_pkgname/tools/$_gitname
}
