# Maintainer: Jingbei Li <i@jingbei.lli>
pkgname='kaldi-kaldi_lm'
_pkgname='kaldi'
pkgdesc='Speech recognition research toolkit'
pkgver=20160109
pkgrel=1
makedepends=('git' 'wget' 'python' 'python2' 'subversion')
depends=('perl')
arch=('x86_64' 'i686')
url='https://github.com/kaldi-asr/kaldi'
license=('APACHE')
source=("https://github.com/kaldi-asr/kaldi/archive/master.zip"
"http://www.danielpovey.com/files/kaldi/kaldi_lm.tar.gz")
sha256sums=('ff40262d37b37f9d1f222e38ac52ccecc4f91295a1eda13e26eafa9f7a0c45da'
            'a43adc7992502546f08158f33b93c66fa91855c86822fe83795de34c8fe7e2b0')

pkgver(){
	cd kaldi_lm
	stat -c %y * | cut -d' ' -f1 | sort | tail -n1 | sed 's/-//g'
}

build () {
	cd $srcdir/$_pkgname-master/tools
	extras/install_kaldi_lm.sh
	#chmod +rx kaldi_lm
}

package () {
	cd $srcdir/$_pkgname-master/tools
	rm kaldi_lm/{*.cc,Makefile}

	mkdir -p $pkgdir/opt/$_pkgname/tools/
	cp -r kaldi_lm $pkgdir/opt/$_pkgname/tools/
}
