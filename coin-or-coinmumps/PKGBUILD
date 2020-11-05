pkgname=coin-or-coinmumps
pkgver=1.6.2
pkgrel=1
pkgdesc="COIN-OR autotools harness to build MUMPS"
arch=('x86_64')
url="https://github.com/coin-or-tools/ThirdParty-MUMPS/"
license=('custom')
groups=('coin-or')
depends=('metis' 'blas')
makedepends=('gcc-fortran' 'wget')
source=("https://github.com/coin-or-tools/ThirdParty-Mumps/archive/releases/$pkgver.tar.gz")
sha256sums=('0cfdd30b9cb42d9539ad9c495629f56dd1fc0b59cea691bbe71a129fabd8895d')

prepare () {
  cd "ThirdParty-Mumps-releases-$pkgver"
  ./get.Mumps
}

build() {
  cd "ThirdParty-Mumps-releases-$pkgver"
  FFLAGS="-fallow-argument-mismatch" ./configure --prefix=/usr
  make
}

package() {
    cd "ThirdParty-Mumps-releases-$pkgver"
    PKG_CONFIG_LIBDIR="${pkgdir}/usr/lib/pkgconfig/" \
    make DESTDIR="${pkgdir}" install
}
