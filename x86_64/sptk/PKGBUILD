# Maintainer: Jingbei Li <i@jingbei.li>
# Contributor: Moritz Maxeiner <moritz@ucworks.org>
# Contributor: Sebastien <sebcactus@gmail.com>
pkgname=sptk
pkgver=3.11
pkgrel=1
pkgdesc="A suite of speech signal processing tools."
arch=('x86_64')
url="http://sp-tk.sourceforge.net/"
license=('BSD')
depends=('glibc')
makedepends=('tcsh')
optdepends=('libx11: for XY-plotter' 'tcsh: for helper scripts')
source=(http://downloads.sourceforge.net/sp-tk/SPTK-$pkgver.tar.gz ${pkgname}.sh)
sha256sums=('ae26929a3c196ca8a1d1a638718fc4400adf8ce963b8328be72f8802f1589100'
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
