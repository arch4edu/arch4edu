# Maintainer: Jingbei Li <i@jingbei.li>
# Contributor: Moritz Maxeiner <moritz@ucworks.org>
# Contributor: Sebastien <sebcactus@gmail.com>

pkgname=sptk
pkgver=3.10
pkgrel=1
pkgdesc="A suite of speech signal processing tools."
arch=('x86_64')
url="http://sp-tk.sourceforge.net/"
license=('BSD')
depends=('glibc')
makedepends=('tcsh')
optdepends=('libx11: for XY-plotter' 'tcsh: for helper scripts')
source=(http://downloads.sourceforge.net/sp-tk/SPTK-$pkgver.tar.gz ${pkgname}.sh)
sha256sums=('a9bf59df6eb798eed3c6c08dac0443db25e4675e700235486add45a17d4ed9fe'
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
