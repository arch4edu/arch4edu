# Maintainer: Markus Näther <naetherm@informatik.uni-freiburg.de>
# Maintainer: acxz <akashpatel2008 at yahoo dot com>

pkgname=hipsparse
pkgver=4.0.0
pkgrel=1
pkgdesc='rocSPARSE marshalling library.'
arch=('x86_64')
url='https://rocmdocs.amd.com/en/latest/ROCm_Libraries/ROCm_Libraries.html#hipsparse'
license=('MIT')
depends=('hip-rocclr' 'rocsparse')
makedepends=('cmake' 'git' 'gcc-fortran')
_git='https://github.com/ROCmSoftwarePlatform/hipSPARSE'
source=("$pkgname-$pkgver.tar.gz::$_git/archive/rocm-$pkgver.tar.gz")
sha256sums=('fc3736b2ea203209021616b2ffbcdd664781d692b07b8e8bb7f78b42dabbd5e5')
_dirname="$(basename "$_git")-$(basename "${source[0]}" ".tar.gz")"

build() {
  CXX=/opt/rocm/hip/bin/hipcc \
  cmake -Wno-dev -S "$_dirname" \
        -DCMAKE_CXX_STANDARD=20 \
        -DCMAKE_INSTALL_PREFIX=/opt/rocm \
        -Damd_comgr_DIR=/opt/rocm/lib/cmake/amd_comgr \
        -DAMDDeviceLibs_DIR=/opt/rocm/lib/cmake/AMDDeviceLibs \
        -Dhip_DIR=/opt/rocm/hip/lib/cmake/hip \
        -Drocsparse_DIR=/opt/rocm/rocsparse/lib/cmake/rocsparse \
        -DBUILD_CLIENTS_SAMPLES=OFF \
        -DBUILD_CLIENTS_TESTS=OFF
  make
}

package() {
  DESTDIR="$pkgdir" make install

  install -Dm644 /dev/stdin "$pkgdir/etc/ld.so.conf.d/hipsparse.conf" << EOF
/opt/rocm/hipsparse/lib
EOF
  install -Dm644 "$srcdir/hipSPARSE-rocm-$pkgver/LICENSE.md" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
