# Maintainer: Jingbei Li <i@jingbei.lli>
pkgname='kaldi-openfst'
_pkgname='kaldi'
pkgdesc='Speech recognition research toolkit'
pkgver=1.6.7
pkgrel=2
depends=('gcc-libs')
makedepends=('git' 'wget' 'python' 'python2' 'subversion' 'unzip' 'sox' 'gcc-fortran')
arch=('x86_64' 'i686')
url='https://github.com/kaldi-asr/kaldi'
license=('APACHE')
source=("https://github.com/kaldi-asr/kaldi/archive/master.zip")
sha256sums=('SKIP')

build () {
	cd $srcdir/$_pkgname-master/tools
	mkdir -p python
	touch python/.use_default_python
	make openfst
}

package () {
	mkdir -p $pkgdir/opt/$_pkgname/tools/openfst-$pkgver
	cd $pkgdir/opt/$_pkgname/tools
	ln -s openfst-$pkgver openfst
	cp -r $srcdir/$_pkgname-master/tools/openfst-$pkgver/{bin,include,lib,Makefile} openfst-$pkgver
}
