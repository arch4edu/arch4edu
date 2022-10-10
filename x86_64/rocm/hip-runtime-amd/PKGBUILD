# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: acxz <akashpatel2008 at yahoo dot com>
pkgname=hip-runtime-amd
pkgver=5.3.0
pkgrel=1
pkgdesc="Heterogeneous Interface for Portability ROCm"
arch=('x86_64')
url='https://rocmdocs.amd.com/en/latest/Installation_Guide/HIP.html'
license=('MIT')
depends=('mesa' 'comgr' 'rocminfo' 'rocm-llvm' 'libelf')
makedepends=('cmake' 'python')
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
sha256sums=('05225832fb5a4d24f49a773ac27e315239943a6f24291a50d184e2913f2cdbe0'
            'd251e2efe95dc12f536ce119b2587bed64bbda013969fa72be58062788044a9e'
            '2bf14116b5e2270928265f5d417b3d0f0f2e13cbc8ec5eb8c80d4d4a58ff7e94'
            '81e9bd5209a7b400c986f9bf1d7079bcf7169bbcb06fc4fe843644559a4d612e')
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
    -DHIP_COMMON_DIR="$srcdir/$_dirhip" \
    -DAMD_OPENCL_PATH="$srcdir/$_diropencl" \
    -DROCCLR_PATH="$srcdir/$_dirrocclr" \
    -DHIP_PLATFORM=amd \
    -DCMAKE_INSTALL_PREFIX=/opt/rocm

  cmake --build .
}

package() {
  DESTDIR="$pkgdir" cmake --install build

  install -Dm644 "$srcdir/HIP-rocm-$pkgver/LICENSE.txt" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
  echo '/opt/rocm/hip/lib' > "$pkgname.conf"
  install -Dm644 "$pkgname.conf" "$pkgdir/etc/ld.so.conf.d/$pkgname.conf"
}
