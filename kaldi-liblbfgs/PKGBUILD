# Maintainer: Jingbei Li <i@jingbei.li>
pkgname='kaldi-liblbfgs'
_pkgname='kaldi'
pkgdesc='Speech recognition research toolkit'
pkgver=1.10
pkgrel=1
makedepends=('git' 'wget' 'python' 'python2' 'subversion')
depends=('glibc')
arch=('x86_64' 'i686')
url='https://github.com/kaldi-asr/kaldi'
license=('APACHE')
source=("https://github.com/kaldi-asr/kaldi/archive/master.zip")
sha256sums=('SKIP')

build () {
	cd $srcdir/$_pkgname-master/tools
	ln -sf $srcdir/srilm.tgz .
	sh extras/install_liblbfgs.sh
}

package () {
	cd $srcdir/$_pkgname-master/tools/liblbfgs-$pkgver
	find . -maxdepth 1 -type f -exec rm {} \;
	rm -r share sample lib/{.libs,.deps,*.a,*.la,*.o,*.lo,*.c,Makefile*,lib.vcxproj}
	mkdir -p $pkgdir/opt/$_pkgname/tools/liblbfgs-$pkgver
	cp -r include lib $pkgdir/opt/$_pkgname/tools/liblbfgs-$pkgver
}
