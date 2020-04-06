# Maintainer: Markus Näther <naetherm@cs.uni-freiburg.de>
# Contributor: fermyon <antifermion@protonmail.com>
# Contributor: Ranieri Althoff <ranisalt+aur at gmail.com>

pkgname=rocm-cmake
pkgver=3.3.0
pkgrel=1
pkgdesc='CMake modules for common build tasks needed for the ROCm software stack'
arch=('x86_64')
url='https://github.com/RadeonOpenCompute/rocm-cmake'
license=('MIT')
makedepends=('cmake')
source=("$url/archive/rocm-$pkgver.tar.gz")
sha256sums=('76ed3ee8e56cf3246011cf7723c2abda539e1136e7e7f6909bfa45d268b8644f')
_dirname="$(basename "$url")-$(basename "${source[0]}" .tar.gz)"

build() {
  cmake -DCMAKE_INSTALL_PREFIX=/opt/rocm "$_dirname"
}

package() {
  make DESTDIR="$pkgdir" install
}
