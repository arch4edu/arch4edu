# Maintainer: Jingbei Li <i@jingbei.lli>
_pkgname='kaldi'
_gitname='irstlm'
pkgname="$_pkgname-$_gitname"
pkgdesc='Speech recognition research toolkit'
pkgver=r94.c358d7b
pkgrel=1
makedepends=('git' 'wget' 'python' 'python2' 'subversion')
arch=('x86_64' 'i686')
url='https://github.com/kaldi-asr/kaldi'
license=('APACHE')
source=("git+https://github.com/irstlm-team/irstlm"
"https://github.com/kaldi-asr/kaldi/archive/master.zip")
sha256sums=('SKIP' 'SKIP')

pkgver () {
	cd "${_gitname}"
	(
		set -o pipefail
		printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
	)
}

build () {
	cd $srcdir/$_pkgname-master/tools
	cp -r $srcdir/$_gitname .
	extras/install_irstlm.sh
}

package () {
	mkdir -p $pkgdir/opt/$_pkgname/tools/$_gitname
	cp -r $srcdir/$_pkgname-master/tools/$_gitname/{bin,include,lib} $pkgdir/opt/$_pkgname/tools/$_gitname
}
