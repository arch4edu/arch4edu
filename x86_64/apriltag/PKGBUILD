# Maintainer: Atakku <atakkudev@gmail.com>
pkgname=apriltag
pkgver=3.2.0
pkgrel=3
pkgdesc="AprilTag is a visual fiducial system popular for robotics research."
arch=('x86_64')
url="https://april.eecs.umich.edu/software/apriltag"
license=('BSD')
makedepends=('cmake')
source=("https://github.com/AprilRobotics/apriltag/archive/v${pkgver}.tar.gz"
        "cmake.patch")
sha512sums=('0b09b530ed03dce0bdc3c4e08b17d98f1303ab1d45870843354bf1a5bdf6c7efc6089e2bdf40a370d17a8191b7ce2c46fefa2dd2d49a959591351e00e186f33e'
            '0851483ebaadab808349927a0ff308c649902a10f4067fd193dfa7f4ec6c7cc11850ac2905a6bdcf7a1287924a0e9c9752f6ec52e732c2158fcf58ec4763ea7f')

prepare() {
  mkdir -p "$srcdir/build"

  cd "$srcdir/${pkgname}-${pkgver}"
  #patch -Np1 -i "$srcdir/cmake.patch"
}


build() {
  cd "$srcdir/build"
  cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=/usr \
    "$srcdir/${pkgname}-${pkgver}"
}

package() {
  cd "$srcdir/build"
  make VERBOSE=1 DESTDIR="$pkgdir" install
}
