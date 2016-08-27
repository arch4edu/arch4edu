# Maintainer: Moritz Maxeiner <moritz@ucworks.org>
# Contributor: Sebastien <sebcactus@gmail.com>

pkgname=sptk
pkgver=3.8
pkgrel=1
pkgdesc="A suite of speech signal processing tools."
arch=('any')
url="http://sp-tk.sourceforge.net/"
license=('BSD')
depends=('glibc')
makedepends=('tcsh')
optdepends=('libx11: for XY-plotter' 'tcsh: for helper scripts')
source=(http://downloads.sourceforge.net/sp-tk/SPTK-$pkgver.tar.gz ${pkgname}.sh)
sha256sums=('028d6b3230bee73530f3d67d64eafa32cf23eaa987545975d260d0aaf6953f2b'
            'b5afaf60414297bd359f73dbe14ae2a3608f9c52301cc5801c9708ceb710d416')
build()
{
  cd "${srcdir}/SPTK-$pkgver"
  ./configure --prefix=/opt/$pkgname
  make
}

package()
{
  cd "${srcdir}/SPTK-$pkgver"
  make prefix="${pkgdir}/opt/$pkgname" install
  install -D -m644 COPYING "${pkgdir}/usr/share/licenses/${pkgname}/COPYING"
  install -D -m755 ../${pkgname}.sh "${pkgdir}/etc/profile.d/${pkgname}.sh"
}
