# Maintainer: Jingbei Li <i@jingbei.lli>
pkgname=kaldi-openfst
_pkgname=kaldi
pkgdesc='Speech recognition research toolkit'
pkgver=1.8.4
pkgrel=1
depends=(gcc-libs)
makedepends=(gcc-fortran git python sox subversion unzip wget)
arch=('x86_64')
url='https://github.com/kaldi-asr/kaldi'
license=('APACHE')
options=(!lto)
_commit='01aadd7c19372e3eacadec88caabd86162f33d69'
source=("${url}/archive/${_commit}.tar.gz")
sha256sums=('b7f6789806e5d8015bfaa1940cebfc5ed59251988f31dd162e2c4382ec523829')

build () {
	cd $srcdir/$_pkgname-$_commit/tools
	mkdir -p python
	touch python/.use_default_python
	make openfst
}

package () {
	mkdir -p $pkgdir/opt/$_pkgname/tools/openfst-$pkgver
	cd $pkgdir/opt/$_pkgname/tools
	ln -s openfst-$pkgver openfst
	cp -r $srcdir/$_pkgname-$_commit/tools/openfst-$pkgver/{bin,include,lib,Makefile} openfst-$pkgver
}
