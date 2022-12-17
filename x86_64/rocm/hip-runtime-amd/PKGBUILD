# Maintainer: Torsten Keßler <tpkessler at archlinux dot org>
# Contributor: acxz <akashpatel2008 at yahoo dot com>
pkgname=hip-runtime-amd
pkgver=5.4.1
pkgrel=1
pkgdesc="Heterogeneous Interface for Portability ROCm"
arch=('x86_64')
url='https://docs.amd.com/bundle/HIP-Programming-Guide-v5.4/page/Introduction_to_HIP_Programming_Guide.html'
license=('MIT')
depends=('mesa' 'comgr' 'rocminfo' 'rocm-llvm' 'libelf')
makedepends=('cmake' 'python' 'python-cppheaderparser')
provides=('hip')
conflicts=('hip')
_hip='https://github.com/ROCm-Developer-Tools/HIP'
_opencl='https://github.com/RadeonOpenCompute/ROCm-OpenCL-Runtime'
_rocclr='https://github.com/ROCm-Developer-Tools/ROCclr'
_hipamd='https://github.com/ROCm-Developer-Tools/hipamd'
source=("$pkgname-$pkgver.tar.gz::$_hip/archive/rocm-$pkgver.tar.gz"
        "$pkgname-opencl-$pkgver.tar.gz::$_opencl/archive/rocm-$pkgver.tar.gz"
        "$pkgname-rocclr-$pkgver.tar.gz::$_rocclr/archive/rocm-$pkgver.tar.gz"
        "$pkgname-hipamd-$pkgver.tar.gz::$_hipamd/archive/rocm-$pkgver.tar.gz")
sha256sums=('12e82877b55324f1910e760f4c5ec105bf6547b69215997d8d098fc463d399c3'
            '2b3d7b365f569ce64d1408d6e745d005aa10eca3623891be50f6b1b2e802d875'
            'c0926fa5dad71cd02f21504d82e218d482779df579a400604e13864e6b2a7d9c'
            '8ca75fa4a472dfbc8059b7f5ad717466c0db544c516950b3fa32c5de32980216')
_dirhip="$(basename "$_hip")-$(basename "${source[0]}" ".tar.gz")"
_diropencl="$(basename "$_opencl")-$(basename "${source[1]}" ".tar.gz")"
_dirrocclr="$(basename "$_rocclr")-$(basename "${source[2]}" ".tar.gz")"
_dirhipamd="$(basename "$_hipamd")-$(basename "${source[3]}" ".tar.gz")"

build() {
  # build fails if cmake and make are called from outside the build directory
  mkdir build && cd build

  # Disable assertations as a temporary workaround for hipRTC
  # https://github.com/ROCmSoftwarePlatform/rocFFT/issues/389#issuecomment-1341370581
  CXXFLAGS="$CXXFLAGS -DNDEBUG" \
  cmake \
    -Wno-dev \
    -S "$srcdir/$_dirhipamd" \
    -DHIP_COMMON_DIR="$srcdir/$_dirhip" \
    -DAMD_OPENCL_PATH="$srcdir/$_diropencl" \
    -DROCCLR_PATH="$srcdir/$_dirrocclr" \
    -DHIP_PLATFORM=amd \
    -DCMAKE_BUILD_TYPE=None \
    -DROCM_DIR=/opt/rocm \
    -DCMAKE_INSTALL_PREFIX=/opt/rocm

  cmake --build .
}

package() {
  DESTDIR="$pkgdir" cmake --install build

  install -Dm644 "$srcdir/$_dirhip/LICENSE.txt" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
  echo '/opt/rocm/hip/lib' > "$pkgname.conf"
  install -Dm644 "$pkgname.conf" "$pkgdir/etc/ld.so.conf.d/$pkgname.conf"
}
