# Maintainer: shtrophic <aur at shtrophic dot net>
# Contributor: Atakku <atakkudev@gmail.com>

pkgbase=apriltag
pkgname=($pkgbase python-$pkgbase)
pkgver=3.4.3
pkgrel=1
pkgdesc="visual fiducial system popular for robotics research"
arch=('x86_64')
url="https://april.eecs.umich.edu/software/apriltag"
license=('BSD-2-Clause')
makedepends=('cmake'
             'python-numpy')
source=("https://github.com/AprilRobotics/apriltag/archive/v${pkgver}.tar.gz")
b2sums=('e25dd2da60451daa45dfd45522ebbb18469b09f2376bf44880029fede25f3def4af2fa889b77f1aa8e21beb338ee39b849275420df599c96079c89e813ab2fac')

build() {
  cd "$srcdir"
  cmake -B build \
    -DCMAKE_BUILD_TYPE=None \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -Wno-dev \
    -DBUILD_EXAMPLES=OFF \
    -DBUILD_TESTING=ON \
    -DBUILD_PYTHON_WRAPPER=ON \
    "$srcdir/${pkgbase}-${pkgver}"
  cmake --build build
}

check() {
  cd "$srcdir"
  datadir="$pkgbase-$pkgver/test/data"
  for img in $(find $datadir -name '*.jpg'); do
    build/test/test_detection "$datadir/$(basename -s .jpg $img)"
  done
}

package_apriltag() {
  local pysitedir=$(python -c 'import site; print(site.getsitepackages()[0])')
  cd "$srcdir"
  DESTDIR="$pkgdir" cmake --install build
  mkdir -p "$pkgdir/usr/lib/cmake/$pkgbase"
  mv "$pkgdir/usr/lib/apriltag/cmake"/* "$pkgdir/usr/lib/cmake/$pkgbase"
  mv "$pkgdir/usr/lib/cmake/$pkgbase/apriltagConfig"{Version,-version}.cmake
  rm -rf "$pkgdir/usr/share"
  rm -rf "$pkgdir/$(dirname $pysitedir)"
  rm -rf "$pkgdir/usr/lib/apriltag"
}

package_python-apriltag() {
  pkgdesc="$pkgdesc (python bindings)"
  depends=('apriltag' 'python-numpy')

  local pysitedir=$(python -c 'import site; print(site.getsitepackages()[0])')
  install -Dm 644 build/apriltag.cpython-*-x86_64-linux-gnu.so -t "$pkgdir/$pysitedir"
}
