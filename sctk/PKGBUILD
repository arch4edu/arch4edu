# Maintainer: Jingbei Li <i@jingbei.lli>
pkgname='sctk'
pkgdesc='Speech Recognition Scoring Toolkit (SCTK)'
pkgver=2.4.10
_tag='20151007-1312Z'
pkgrel=1
depends=('perl')
arch=('x86_64' 'i686')
url='https://www.nist.gov/itl/iad/mig/tools'
license=('APACHE')
source=("ftp://jaguar.ncsl.nist.gov/pub/sctk-${pkgver}-${_tag}.tar.bz2")
sha512sums=('1f97a619ed7c3032698c541536e10c1fb1cb29ca34b899e13c00e48c8cccdc0db7c9e024224460604760cf82ece32bd325642fe9bd975abba7f460f273871cf0')

build () {
	cd $srcdir/$pkgname-$pkgver
	sed "/^PREFIX=/s/^.*$/PREFIX=${pkgdir//\//\\\/}\/opt\/$pkgname/" -i src/makefile
	make config
	sed '/^DEFS/s/ -Dsize_t=unsigned//' -i src/sclite/makefile
	make all
}

package () {
	cd $srcdir/$pkgname-$pkgver
	mkdir -p $pkgdir/opt/$pkgname/bin
	make install
	make doc
	cp -r doc $pkgdir/opt/$pkgname
}
