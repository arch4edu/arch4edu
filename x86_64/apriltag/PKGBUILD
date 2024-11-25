# Maintainer: shtrophic <aur at shtrophic dot net>
# Contributor: Atakku <atakkudev@gmail.com>

pkgname=(apriltag python-apriltag)
pkgver=3.4.2
pkgrel=1
pkgdesc="AprilTag is a visual fiducial system popular for robotics research"
arch=('x86_64')
url="https://april.eecs.umich.edu/software/apriltag"
license=('BSD')
makedepends=('cmake'
             'python-numpy')
source=("https://github.com/AprilRobotics/apriltag/archive/v${pkgver}.tar.gz")
sha512sums=('2e7edda62e1f196ac954cb999d11a43e81e4e8a5de296b7ce28744a0ec3a4a3209b413e2328aaebce61b2eef782209855ca1112c489bbcb5437387ab6379a849')

build() {
  cd "$srcdir"
  cmake -B build \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -Wno-dev \
    -DBUILD_EXAMPLES=OFF \
    -DBUILD_TESTING=ON \
    "$srcdir/${pkgname}-${pkgver}"
  cmake --build build
}

check() {
  cd "$srcdir"
  datadir="apriltag-$pkgver/test/data"
  for img in $(find $datadir -name '*.jpg')
  do
    build/test/test_detection "$datadir"/$(basename -s .jpg $img) > /dev/null
  done
}

package_apriltag() {
  cd "$srcdir"
  DESTDIR="$pkgdir" cmake --install build
  mkdir -p "$pkgdir/usr/lib/cmake/$pkgname"
  mv "$pkgdir/usr/share/$pkgname/cmake"/* "$pkgdir/usr/lib/cmake/$pkgname"
  mv "$pkgdir/usr/lib/cmake/$pkgname/apriltagConfig"{Version,-version}.cmake
  rm -rf "$pkgdir/usr/share"
  rm -rf "$pkgdir/usr/lib/python3.12"
}

package_python-apriltag() {
  pkgdesc="$pkgdesc"' (python bindings)'
  depends=('apriltag' 'python-numpy')
  install -Dm 644 "build/apriltag.cpython-312-x86_64-linux-gnu.so" -t "$pkgdir"/usr/lib/python3.12/site-packages
}
