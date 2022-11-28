# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: acxz <akashpatel2008 at yahoo dot com>
pkgname=hip-runtime-amd
pkgver=5.3.3
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
sha256sums=('51d4049dc37d261afb9e1270e60e112708ff06b470721ff21023e16e040e4403'
            'cab394e6ef16c35bab8de29a66b96a7dc0e7d1297aaacba3718fa1d369233c9f'
            'f8133a5934f9c53b253d324876d74f08a19e2f5b073bc94a62fe64b0d2183a18'
            '36acce92af39b0fa06002e164f5a7f5a9c7daa19bf96645361325775a325499d')
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
