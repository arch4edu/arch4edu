# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: acxz <akashpatel2008 at yahoo dot com>
pkgname=hip-runtime-amd
pkgver=5.2.0
pkgrel=2
pkgdesc="Heterogeneous Interface for Portability ROCm"
arch=('x86_64')
url='https://rocmdocs.amd.com/en/latest/Installation_Guide/HIP.html'
license=('MIT')
depends=('mesa' 'comgr' 'rocminfo' 'rocm-llvm' 'libelf')
makedepends=('cmake' 'python' 'git')
provides=('hip')
conflicts=('hip')
_hip='https://github.com/ROCm-Developer-Tools/HIP'
_opencl='https://github.com/RadeonOpenCompute/ROCm-OpenCL-Runtime'
_rocclr='https://github.com/ROCm-Developer-Tools/ROCclr'
_hipamd='https://github.com/ROCm-Developer-Tools/hipamd'
source=("$pkgname-$pkgver.tar.gz::$_hip/archive/rocm-$pkgver.tar.gz"
        "$pkgname-opencl-$pkgver.tar.gz::$_opencl/archive/rocm-$pkgver.tar.gz"
        "$pkgname-rocclr-$pkgver.tar.gz::$_rocclr/archive/rocm-$pkgver.tar.gz"
        "$pkgname-hipamd-$pkgver.tar.gz::$_hipamd/archive/rocm-$pkgver.tar.gz"
        "git-hash.patch"
        "config-path.patch::https://patch-diff.githubusercontent.com/raw/ROCm-Developer-Tools/hipamd/pull/32.patch")
sha256sums=('a6e0515d4d25865c037b546035df9c51f0882cd2700e759c266ff7e199f37c3a'
            '80f73387effdcd987a150978775a87049a976aa74f5770d4420847b004dd59f0'
            '37f5fce04348183bce2ece8bac1117f6ef7e710ca68371ff82ab08e93368bafb'
            '8774958bebc29a4b7eb9dc2d38808d79d9a24bf9c1f44e801ff99d2d5ba82240'
            '84cd40751e041edd48489eca59f1702bba08a402b25162e4cf061de45abc2bde'
            'SKIP')
_dirhip="$(basename "$_hip")-$(basename "${source[0]}" ".tar.gz")"
_diropencl="$(basename "$_opencl")-$(basename "${source[1]}" ".tar.gz")"
_dirrocclr="$(basename "$_rocclr")-$(basename "${source[2]}" ".tar.gz")"
_dirhipamd="$(basename "$_hipamd")-$(basename "${source[3]}" ".tar.gz")"

prepare() {
    cd "$_dirhipamd"
    patch -Np1 -i "$srcdir/git-hash.patch"
    patch -N   -i "$srcdir/config-path.patch"
}

build() {
  local cmake_args=(-DHIP_COMMON_DIR="$srcdir/$_dirhip"
                    -DHIP_COMMON_DIR="$srcdir/$_dirhip"
                    -DAMD_OPENCL_PATH="$srcdir/$_diropencl"
                    -DROCCLR_PATH="$srcdir/$_dirrocclr"
                    -DHIP_PLATFORM=amd
                    -DCMAKE_INSTALL_PREFIX=/opt/rocm)
  if [[ -n "$AMDGPU_TARGETS" ]]; then
      cmake_args+=(-DAMDGPU_TARGETS="${AMDGPU_TARGETS}")
  fi

  # build fails if cmake and make are called from outside the build directory
  mkdir build && cd build
  cmake -Wno-dev \
  -S "$srcdir/$_dirhipamd" \
  "${cmake_args[@]}"

  make
}

package() {
  DESTDIR="$pkgdir" make -C build install

  # https://github.com/ROCm-Developer-Tools/HIP/issues/2678
  sed -i '/__noinline__/d' "$pkgdir/opt/rocm/hip/include/hip/amd_detail/host_defines.h"

  # add links (hipconfig is for rocblas with tensile)
  install -d "$pkgdir/usr/bin"
  local _fn
  for _fn in hipcc hipconfig hipcc.pl hipconfig.pl; do
    ln -s "/opt/rocm/hip/bin/$_fn" "$pkgdir/usr/bin/$_fn"
  done
 
  install -Dm644 /dev/stdin "$pkgdir/etc/ld.so.conf.d/hip.conf" <<EOF
/opt/rocm/hip/lib
EOF
  install -Dm644 "$srcdir/HIP-rocm-$pkgver/LICENSE.txt" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
