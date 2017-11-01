# Maintainer: Jingbei Li <i@jingbei.lli>
pkgname='kaldi-srilm'
_pkgname='kaldi'
pkgdesc='Speech recognition research toolkit'
pkgver=1.7.2
_liblbfgs_ver=1.10
pkgrel=1
makedepends=('git' 'wget' 'python' 'python2' 'subversion')
depends=('kaldi-liblbfgs')
arch=('x86_64' 'i686')
url='https://github.com/kaldi-asr/kaldi'
license=('APACHE')
source=("https://github.com/kaldi-asr/kaldi/archive/master.zip"
"srilm.tgz::https://www.dropbox.com/s/41y27or8lco4fju/srilm-$pkgver.tar.gz?dl=1")
noextract=('srilm.tgz')
sha256sums=('SKIP'
'a528a778f881c679233f94d7b26d6f795129fa6009b32305c8ce769f66e223b4')

build () {
	cd $srcdir/$_pkgname-master/tools
	ln -sf $srcdir/srilm.tgz .
	ln -sf /opt/kaldi/tools/liblbfgs-$_liblbfgs_ver .
	extras/install_srilm.sh
}

package () {
	cd $srcdir/$_pkgname-master/tools/srilm
	find . -maxdepth 1 -type f -exec rm {} \;
	find . \
		-name '*.cc' \
		-or -name '*.~*' \
		-or -name '*.mk' \
		-exec rm -f {} \;
	mkdir -p $pkgdir/opt/$_pkgname/tools/srilm
	cp -r bin lib include $pkgdir/opt/$_pkgname/tools/srilm
}
