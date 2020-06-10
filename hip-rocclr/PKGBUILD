# Maintainer: acxz <akashpatel2008 at yahoo dot com>
pkgname=hip-rocclr
pkgver=3.5.0
pkgrel=1
pkgdesc="Heterogeneous Interface for Portability ROCm"
arch=('x86_64')
url='https://rocmdocs.amd.com/en/latest/Installation_Guide/HIP.html'
license=('MIT')
depends=('rocclr')
makedepends=('libelf' 'cmake' 'python' 'llvm-amdgpu' 'git')
provides=('hip')
conflicts=('hip')
_git='https://github.com/ROCm-Developer-Tools/HIP'
source=("$pkgname-$pkgver.tar.gz::$_git/archive/rocm-$pkgver.tar.gz")
sha256sums=('ae8384362986b392288181bcfbe5e3a0ec91af4320c189bd83c844ed384161b3')

build() {
  mkdir -p build
  cd build
  
  cmake -DCMAKE_INSTALL_PREFIX=/opt/rocm/hip \
        -DHIP_COMPILER=clang \
        -DHIP_PLATFORM=rocclr \
        -DROCCLR_DIR=/opt/rocm/rocclr \
        "$srcdir/HIP-rocm-$pkgver"
  make
}

package() {
  cd build

  make DESTDIR="$pkgdir" install

  # add links (hipconfig is for rocblas with tensile)
  install -d "$pkgdir/usr/bin"
  local _fn
  for _fn in hipcc hipconfig; do
    ln -s "/opt/rocm/hip/bin/$_fn" "$pkgdir/usr/bin/$_fn"
  done

  install -Dm644 /dev/stdin "$pkgdir/etc/ld.so.conf.d/hip.conf" <<EOF
/opt/rocm/hip/lib
EOF
  install -Dm644 "$srcdir/HIP-rocm-$pkgver/LICENSE.txt" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
