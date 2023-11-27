# Maintainer: robertfoster
pkgname=smpq
pkgver=1.6
pkgrel=2
pkgdesc="StormLib MPQ archiving utility. Designed for full manipulating with Blizzard MPQ archives"
arch=('i686' 'x86_64')
url="https://launchpad.net/smpq"
license=('GPL3')
depends=('bzip2' 'stormlib' 'zlib')
makedepends=('cmake')
source=("https://launchpad.net/smpq/trunk/${pkgver}/+download/smpq_${pkgver}.orig.tar.gz"
  fix-smpq-compilation.patch
)

prepare() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  patch -Np1 -i ../fix-smpq-compilation.patch
  if [ ! -d build ]; then
    mkdir build
  fi
}

build() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  cd build
  cmake -DWITH_KDE=OFF \
    -DCMAKE_INSTALL_PREFIX=/usr ..
  make
}

package() {
  cd "$pkgname-$pkgver"
  cd build
  make DESTDIR="$pkgdir/" install
}

sha256sums=('b5d2dc8a5de8629b71ee5d3612b6e84d88418b86c5cd39ba315e9eb0462f18cb'
            '6152abe9a75d539e9a8386126b11875da8a7cd82b2805d0a97e643348dcdca5f')
