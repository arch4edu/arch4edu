# Maintainer: Jingbei Li <i@jingbei.li>
# Contributor: Moritz Maxeiner <moritz@ucworks.org>
# Contributor: Sebastien <sebcactus@gmail.com>
pkgname=sptk
pkgver=4.0
pkgrel=1
pkgdesc="A suite of speech signal processing tools."
arch=('x86_64')
url="http://sp-tk.sourceforge.net/"
license=('Apache')
depends=('glibc')
makedepends=('cmake' 'tcsh')
optdepends=('libx11: for XY-plotter' 'tcsh: for helper scripts')
source=("https://github.com/sp-nitech/SPTK/archive/refs/tags/v${pkgver}.tar.gz" ${pkgname}.sh)
sha256sums=('2defd24b1f0b7e857b046d1bba390bbafddcca517a816de633640cb4b5b9f871'
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
