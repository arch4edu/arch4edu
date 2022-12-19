# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: acxz <akashpatel2008 at yahoo dot com>
pkgname=hip-runtime-nvidia
pkgver=5.4.1
pkgrel=1
pkgdesc="Heterogeneous Interface for Portability ROCm"
arch=('x86_64')
url='https://rocmdocs.amd.com/en/latest/Installation_Guide/HIP.html'
license=('MIT')
depends=('cuda' 'rocm-llvm' 'libelf')
makedepends=('cmake' 'python')
provides=('hip')
conflicts=('hip')
_hip='https://github.com/ROCm-Developer-Tools/HIP'
_hipamd='https://github.com/ROCm-Developer-Tools/hipamd'
source=("$pkgname-$pkgver.tar.gz::$_hip/archive/rocm-$pkgver.tar.gz"
        "$pkgname-hipamd-$pkgver.tar.gz::$_hipamd/archive/rocm-$pkgver.tar.gz"
        "nvcc-with-amdclang.patch::https://patch-diff.githubusercontent.com/raw/ROCm-Developer-Tools/HIP/pull/2849.patch")
sha256sums=('12e82877b55324f1910e760f4c5ec105bf6547b69215997d8d098fc463d399c3'
            '8ca75fa4a472dfbc8059b7f5ad717466c0db544c516950b3fa32c5de32980216'
            '0e65a4bbd6edf07dd8785bdf7386de0c2d4eaa6a476e79c7ca33b7662c874eb8')
_dirhip="$(basename "$_hip")-$(basename "${source[0]}" ".tar.gz")"
_dirhipamd="$(basename "$_hipamd")-$(basename "${source[1]}" ".tar.gz")"

prepare() {
    cd "$srcdir/$_dirhip"
    patch -Np1 -i "$srcdir/nvcc-with-amdclang.patch"
}

build() {
  # build fails if cmake and make are called from outside the build directory
  mkdir build && cd build
  cmake \
    -Wno-dev \
    -S "$srcdir/$_dirhipamd" \
    -DHIP_COMMON_DIR="$srcdir/$_dirhip" \
    -DHIP_PLATFORM=nvidia \
    -DCMAKE_BUILD_TYPE=None \
    -DCMAKE_INSTALL_PREFIX=/opt/rocm
  cmake --build .
}

package() {
  DESTDIR="$pkgdir" cmake --install build

  echo '/opt/rocm/lib' > 'hip.conf'
  install -Dm644 "hip.conf" "$pkgdir/etc/ld.so.conf.d/hip.conf"

  install -Dm644 "$srcdir/$_dirhip/LICENSE.txt" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
