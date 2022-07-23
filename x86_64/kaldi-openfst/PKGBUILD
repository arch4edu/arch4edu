# Maintainer: Jingbei Li <i@jingbei.lli>
pkgname=kaldi-openfst
_pkgname=kaldi
pkgdesc='Speech recognition research toolkit'
pkgver=1.7.2
pkgrel=1
depends=(gcc-libs)
makedepends=(gcc-fortran git python python2 sox subversion unzip wget)
arch=('x86_64')
url='https://github.com/kaldi-asr/kaldi'
license=('APACHE')
options=(!lto)

prepare() {
	cd $srcdir
	msg2 "Downloading master.zip..."
	curl -LO "${url}/archive/refs/heads/master.zip"
	bsdtar -xf master.zip
}

pkgver() {
	cd $srcdir/$_pkgname-master/tools
	grep -P '^OPENFST_VERSION \?= ' Makefile | cut -d' ' -f3
}

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
