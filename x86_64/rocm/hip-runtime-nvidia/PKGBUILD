# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: acxz <akashpatel2008 at yahoo dot com>
pkgname=hip-runtime-nvidia
pkgver=5.3.0
pkgrel=3
pkgdesc="Heterogeneous Interface for Portability ROCm"
arch=('x86_64')
url='https://rocmdocs.amd.com/en/latest/Installation_Guide/HIP.html'
license=('MIT')
depends=('cuda' 'rocm-llvm' 'libelf')
makedepends=('cmake' 'python' 'git')
provides=('hip')
conflicts=('hip')
_hip='https://github.com/ROCm-Developer-Tools/HIP'
_hipamd='https://github.com/ROCm-Developer-Tools/hipamd'
source=("$pkgname-$pkgver.tar.gz::$_hip/archive/rocm-$pkgver.tar.gz"
        "$pkgname-hipamd-$pkgver.tar.gz::$_hipamd/archive/rocm-$pkgver.tar.gz"
        "nvcc.patch::https://patch-diff.githubusercontent.com/raw/ROCm-Developer-Tools/HIP/pull/2623.patch")
sha256sums=('05225832fb5a4d24f49a773ac27e315239943a6f24291a50d184e2913f2cdbe0'
            '81e9bd5209a7b400c986f9bf1d7079bcf7169bbcb06fc4fe843644559a4d612e'
            '61bfd113ba81747cabfcc3a6faad00418109050cd28f2abdca6cafa3f936781e')
_dirhip="$(basename "$_hip")-$(basename "${source[0]}" ".tar.gz")"
_dirhipamd="$(basename "$_hipamd")-$(basename "${source[1]}" ".tar.gz")"

prepare() {
    cd "$srcdir/$_dirhip"
    patch -Np1 -i "$srcdir/nvcc.patch"
}

build() {
  # build fails if cmake and make are called from outside the build directory
  mkdir build && cd build
  cmake \
    -Wno-dev \
    -S "$srcdir/$_dirhipamd" \
    -DHIP_COMMON_DIR="$srcdir/$_dirhip" \
    -DHIP_PLATFORM=nvidia \
    -DCMAKE_INSTALL_PREFIX=/opt/rocm
  cmake --build .
}

package() {
  DESTDIR="$pkgdir" cmake --install build

  echo '/opt/rocm/lib' > 'hip.conf'
  install -Dm644 "hip.conf" "$pkgdir/etc/ld.so.conf.d/hip.conf"

  install -Dm644 "$srcdir/$_dirhip/LICENSE.txt" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
