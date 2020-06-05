# Maintainer: Markus Näther <naetherm@cs.uni-freiburg.de>
# Contributor: fermyon <antifermion@protonmail.com>
# Contributor: Ranieri Althoff <ranisalt+aur at gmail.com>

pkgname=rocm-cmake
pkgver=3.5.0
pkgrel=1
pkgdesc='CMake modules for common build tasks needed for the ROCm software stack'
arch=('x86_64')
url='https://github.com/RadeonOpenCompute/rocm-cmake'
license=('MIT')
makedepends=('cmake')
source=("${pkgname}-${pkgver}.tar.gz::$url/archive/rocm-$pkgver.tar.gz")
sha256sums=('5fc09e168879823160f5fdf4fd1ace2702d36545bf733e8005ed4ca18c3e910f')
_dirname="$(basename "$url")-$(basename "${source[0]}" .tar.gz)"

build() {
  cmake -DCMAKE_INSTALL_PREFIX=/opt/rocm "$_dirname"
}

package() {
  make DESTDIR="$pkgdir" install

  install -Dm644 "$_dirname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
