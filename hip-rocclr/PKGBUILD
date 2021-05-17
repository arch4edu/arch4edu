# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: acxz <akashpatel2008 at yahoo dot com>
pkgname=hip-rocclr
pkgver=4.2.0
pkgrel=2
pkgdesc="Heterogeneous Interface for Portability ROCm"
arch=('x86_64')
url='https://rocmdocs.amd.com/en/latest/Installation_Guide/HIP.html'
license=('MIT')
depends=('rocclr' 'rocminfo' 'libelf')
makedepends=('cmake' 'python' 'git')
provides=('hip')
conflicts=('hip')
_git='https://github.com/ROCm-Developer-Tools/HIP'
source=("$pkgname-$pkgver.tar.gz::$_git/archive/rocm-$pkgver.tar.gz"
        'amdgpu-targets.patch')
sha256sums=('ecb929e0fc2eaaf7bbd16a1446a876a15baf72419c723734f456ee62e70b4c24'
            'c1ccea2c6ca3e0e2a5f6449dccab7081386cb224db8c95391b27d8ac6f1d5754')
_dirname="$(basename "$_git")-$(basename "${source[0]}" ".tar.gz")"

prepare() {
    cd "$_dirname"
    patch -Np1 -i "$srcdir/amdgpu-targets.patch"
}

build() {
  CXXFLAGS="$CXXFLAGS -isystem /opt/rocm/include/compiler/lib/include -isystem /opt/rocm/include/elf" \
  cmake -B build -Wno-dev \
        -S "$_dirname" \
        -DCMAKE_INSTALL_PREFIX=/opt/rocm/hip \
        -DCMAKE_PREFIX_PATH=/opt/rocm/lib/cmake \
        -DHIP_COMPILER=clang \
        -DHIP_PLATFORM=rocclr \
        -D__HIP_ENABLE_PCH=OFF
  make -C build
}

package() {
  DESTDIR="$pkgdir" make -C build install

  # add links (hipconfig is for rocblas with tensile)
  install -d "$pkgdir/usr/bin"
  install -d "$pkgdir/opt/rocm/bin"
  local _fn
  for _fn in hipcc hipconfig; do
    ln -s "/opt/rocm/hip/bin/$_fn" "$pkgdir/usr/bin/$_fn"
    ln -s "/opt/rocm/hip/bin/$_fn" "$pkgdir/opt/rocm/bin/$_fn"
  done

  # clang from llvm-amdgpu may look for hipVersion in a different directory
  ln -s '/opt/rocm/hip/bin/.hipVersion' "$pkgdir/opt/rocm/bin/.hipVersion"

  # Some packages search for hip includes in /opt/rocm/include
  install -d "$pkgdir/opt/rocm/include"
  ln -s "/opt/rocm/hip/include/hip" "$pkgdir/opt/rocm/include/hip"

  install -Dm644 /dev/stdin "$pkgdir/etc/ld.so.conf.d/hip.conf" <<EOF
/opt/rocm/hip/lib
EOF
  install -Dm644 "$srcdir/HIP-rocm-$pkgver/LICENSE.txt" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
