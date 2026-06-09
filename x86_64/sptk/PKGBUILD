# Maintainer: Jingbei Li <i@jingbei.li>
# Contributor: Moritz Maxeiner <moritz@ucworks.org>
# Contributor: Sebastien <sebcactus@gmail.com>
pkgname=sptk
pkgver=4.4
pkgrel=1
pkgdesc="A suite of speech signal processing tools."
arch=('x86_64')
url="http://sp-tk.sourceforge.net/"
license=('Apache-2.0')
depends=('glibc')
makedepends=('cmake' 'tcsh')
optdepends=('libx11: for XY-plotter' 'tcsh: for helper scripts')
source=("https://github.com/sp-nitech/SPTK/archive/refs/tags/v${pkgver}.tar.gz" ${pkgname}.sh)
sha256sums=('2a14b37467676fe1bb40f25b2d7b4eaa0f129a8db390be95d8f139a6e060ec3f'
            'b5afaf60414297bd359f73dbe14ae2a3608f9c52301cc5801c9708ceb710d416')
build()
{
  cd "${srcdir}/SPTK-$pkgver"
  mkdir -p build
  cd build
  cmake .. -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX="/opt/$pkgname"
  make
}

package()
{
  cd "${srcdir}/SPTK-$pkgver/build"
  make DESTDIR="${pkgdir}" install
  cd ..
  install -D -m644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
  install -D -m755 ../${pkgname}.sh "${pkgdir}/etc/profile.d/${pkgname}.sh"
}
