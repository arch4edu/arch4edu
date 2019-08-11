# Maintainer: Moritz Maxeiner <moritz@ucworks.org>
# Maintainer: Alexandros Theodotou <alex@zrythm.org>
_tarball=hts_engine_API
pkgname=hts-engine
pkgver=1.10
pkgrel=3
pkgdesc="Engine to synthesize speech waveform from HMMs trained by hts."
arch=('i686' 'x86_64' 'armv7h')
url="http://hts-engine.sourceforge.net/"
license=('BSD')
depends=('glibc')
options=('staticlibs')
source=(https://downloads.sourceforge.net/$pkgname/$_tarball-$pkgver.tar.gz)
md5sums=('5626d1e2522659e93fb295f0b42339f5')
sha256sums=('e2132be5860d8fb4a460be766454cfd7c3e21cf67b509c48e1804feab14968f7')

build()
{
  cd "$srcdir/$_tarball-$pkgver"
  ./configure --prefix=/usr
  make
}

package()
{
  cd "$srcdir/$_tarball-$pkgver"
  make DESTDIR="$pkgdir" prefix="/usr" install
  install -D -m644 COPYING "${pkgdir}/usr/share/licenses/${pkgname}/COPYING"
}
