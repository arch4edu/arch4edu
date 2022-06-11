# Maintainer: Jingbei Li <i@jingbei.lli>
pkgname='kaldi-sph2pipe'
_pkgname='kaldi'
pkgdesc='Speech recognition research toolkit'
pkgver=2.5
pkgrel=2
makedepends=('git' 'wget' 'python' 'python2' 'subversion')
depends=('glibc')
arch=('x86_64' 'i686')
url='https://github.com/kaldi-asr/kaldi'
license=('APACHE')
source=("https://github.com/kaldi-asr/kaldi/archive/master.zip")
sha256sums=('SKIP')

build() {
	cd $srcdir/$_pkgname-master/tools
	make sph2pipe
}

package() {
	install -Dm755 $srcdir/$_pkgname-master/tools/sph2pipe_v$pkgver/sph2pipe $pkgdir/opt/$_pkgname/tools/sph2pipe_v$pkgver/sph2pipe
}
