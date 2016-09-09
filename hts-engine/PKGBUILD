# Maintainer: Moritz Maxeiner <moritz@ucworks.org>
pkgname=hts-engine
pkgver=1.08
pkgrel=1
pkgdesc="Engine to synthesize speech waveform from HMMs trained by hts."
arch=('i686' 'x86_64')
url="http://hts-engine.sourceforge.net/"
license=('BSD')
depends=('glibc')
options=('staticlibs')
source=(http://downloads.sourceforge.net/$pkgname/hts_engine_API-$pkgver.tar.gz)
md5sums=('c0bfe613eb18e5cd923d3a9809716c27')
sha256sums=('9b1dc62dd15346ead364722beb832b8ef93d1c95a3aa5de79b341de510a44638')

build()
{

  cd "$srcdir/hts_engine_API-$pkgver"
  ./configure --prefix=/usr
  make
}

package()
{
  cd "$srcdir/hts_engine_API-$pkgver"
  make prefix="$pkgdir/usr" install
  install -D -m644 COPYING "${pkgdir}/usr/share/licenses/${pkgname}/COPYING"
}
