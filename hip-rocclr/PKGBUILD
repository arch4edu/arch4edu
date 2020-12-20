# Maintainer: acxz <akashpatel2008 at yahoo dot com>
pkgname=hip-rocclr
pkgver=4.0.0
pkgrel=1
pkgdesc="Heterogeneous Interface for Portability ROCm"
arch=('x86_64')
url='https://rocmdocs.amd.com/en/latest/Installation_Guide/HIP.html'
license=('MIT')
depends=('rocclr' 'rocminfo' 'libelf')
makedepends=('cmake' 'python')
provides=('hip')
conflicts=('hip')
_git='https://github.com/ROCm-Developer-Tools/HIP'
source=("$pkgname-$pkgver.tar.gz::$_git/archive/rocm-$pkgver.tar.gz"
        'amdgpu-targets.patch'
        'disable-git-versioning.patch')
sha256sums=('d7b78d96cec67c55b74ea3811ce861b16d300410bc687d0629e82392e8d7c857'
            'c6358b4dfac658c0a27a3425ace455d951cd26be827dd7751c28cb83dc84b67d'
            '7244c2917389788b5ef0265bbd41eef1f0db713debc28d02e3aad9d5a4c79821')
_dirname="$(basename "$_git")-$(basename "${source[0]}" ".tar.gz")"

prepare() {
    cd "$_dirname"
    patch -Np1 -i "$srcdir/amdgpu-targets.patch"
    patch -Np1 -i "$srcdir/disable-git-versioning.patch"
}

build() {
  CXXFLAGS="$CXXFLAGS -isystem /opt/rocm/rocclr/include/compiler/lib/include -isystem /opt/rocm/rocclr/include/elf" \
  cmake -B build -Wno-dev \
        -S "$_dirname" \
        -DCMAKE_INSTALL_PREFIX=/opt/rocm/hip \
        -DCMAKE_PREFIX_PATH='/opt/rocm/lib/cmake/hsa-runtime64;/opt/rocm/lib/cmake/amd_comgr' \
        -DHIP_COMPILER=clang \
        -DHIP_PLATFORM=rocclr \
        -D__HIP_ENABLE_PCH=OFF
  make -C build
}

package() {
  DESTDIR="$pkgdir" make -C build install

  # clang from llvm-amdgpu may look for hipVersion in a different directory
  install -d "$pkgdir/opt/rocm/bin"
  ln -s '/opt/rocm/hip/bin/.hipVersion' "$pkgdir/opt/rocm/bin/.hipVersion"

  # add links (hipconfig is for rocblas with tensile)
  install -d "$pkgdir/usr/bin"
  local _fn
  for _fn in hipcc hipconfig; do
    ln -s "/opt/rocm/hip/bin/$_fn" "$pkgdir/usr/bin/$_fn"
  done
  # Some packages search for hip includes in /opt/rocm/include/hip
  install -d "$pkgdir/opt/rocm/include"
  ln -s "/opt/rocm/hip/include/hip" "$pkgdir/opt/rocm/include/hip"

  install -Dm644 /dev/stdin "$pkgdir/etc/ld.so.conf.d/hip.conf" <<EOF
/opt/rocm/hip/lib
EOF
  install -Dm644 "$srcdir/HIP-rocm-$pkgver/LICENSE.txt" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
