# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: acxz <akashpatel2008 at yahoo dot com>
pkgname=hip-runtime-amd
pkgver=5.4.0
pkgrel=1
pkgdesc="Heterogeneous Interface for Portability ROCm"
arch=('x86_64')
url='https://rocmdocs.amd.com/en/latest/Installation_Guide/HIP.html'
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
sha256sums=('e290f835d69ef23e8b5833a7e616b0a989ff89ada4412d9742430819546efc6c'
            'a294639478e76c75dac0e094b418f9bd309309b07faf6af126cdfad9aab3c5c7'
            '46a1579310b3ab9dc8948d0fb5bed4c6b312f158ca76967af7ab69e328d43138'
            'c4b79738eb6e669160382b6c47d738ac59bd493fc681ca400ff012a2e8212955')
_dirhip="$(basename "$_hip")-$(basename "${source[0]}" ".tar.gz")"
_diropencl="$(basename "$_opencl")-$(basename "${source[1]}" ".tar.gz")"
_dirrocclr="$(basename "$_rocclr")-$(basename "${source[2]}" ".tar.gz")"
_dirhipamd="$(basename "$_hipamd")-$(basename "${source[3]}" ".tar.gz")"

build() {
  # build fails if cmake and make are called from outside the build directory
  mkdir build && cd build

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

  install -Dm644 "$srcdir/HIP-rocm-$pkgver/LICENSE.txt" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
  echo '/opt/rocm/hip/lib' > "$pkgname.conf"
  install -Dm644 "$pkgname.conf" "$pkgdir/etc/ld.so.conf.d/$pkgname.conf"
}
