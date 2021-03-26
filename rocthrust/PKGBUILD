# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: Markus Näther <naetherm@informatik.uni-freiburg.de>
pkgname=rocthrust
pkgver=4.1.0
pkgrel=1
pkgdesc='Port of the Thrust parallel algorithm library atop HIP/ROCm'
arch=('x86_64')
url='https://rocmdocs.amd.com/en/latest/ROCm_Libraries/ROCm_Libraries.html#rocthrust'
license=('Apache')
depends=('hip-rocclr' 'rocprim')
makedepends=('cmake' 'git')
_git='https://github.com/ROCmSoftwarePlatform/rocThrust'
source=("$pkgname-$pkgver.tar.gz::$_git/archive/rocm-$pkgver.tar.gz")
sha256sums=('e3d06c0387a2a6880776c7423b1acf0808fb8833bc822be75793da8c2f521efd')
_dirname="$(basename "$_git")-$(basename "${source[0]}" ".tar.gz")"

build() {
  CXX=/opt/rocm/hip/bin/hipcc \
  cmake -Wno-dev -S "$_dirname" \
        -DCMAKE_INSTALL_PREFIX=/opt/rocm \
        -Damd_comgr_DIR=/opt/rocm/lib/cmake/amd_comgr \
        -DBUILD_TEST=OFF
}

package() {
  DESTDIR="$pkgdir" make install
}
