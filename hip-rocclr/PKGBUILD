# Maintainer: acxz <akashpatel2008 at yahoo dot com>
pkgname=hip-rocclr
pkgver=3.7.0
pkgrel=4
pkgdesc="Heterogeneous Interface for Portability ROCm"
arch=('x86_64')
url='https://rocmdocs.amd.com/en/latest/Installation_Guide/HIP.html'
license=('MIT')
depends=('rocclr' 'libelf')
makedepends=('cmake' 'python' 'git')
provides=('hip')
conflicts=('hip')
_git='https://github.com/ROCm-Developer-Tools/HIP'
source=("$pkgname-$pkgver.tar.gz::$_git/archive/rocm-$pkgver.tar.gz"
        'amdgpu-targets.patch')
sha256sums=('757b392c3beb29beea27640832fbad86681dbd585284c19a4c2053891673babd'
            'c6358b4dfac658c0a27a3425ace455d951cd26be827dd7751c28cb83dc84b67d')
_dirname="$(basename "$_git")-$(basename "${source[0]}" ".tar.gz")"

prepare() {
    cd "$_dirname"
    patch -Np1 -i "$srcdir/amdgpu-targets.patch"
}

build() {
  CXXFLAGS="$CXXFLAGS -isystem /opt/rocm/rocclr/include/compiler/lib/include" \
  cmake -B build -Wno-dev \
        -S "$_dirname" \
        -DCMAKE_INSTALL_PREFIX=/opt/rocm/hip \
        -DCMAKE_PREFIX_PATH='/opt/rocm/lib/cmake/hsa-runtime64;/opt/rocm/lib/cmake/amd_comgr' \
        -DHIP_COMPILER=clang \
        -DHIP_PLATFORM=rocclr
  make -C build
}

package() {
  DESTDIR="$pkgdir" make -C build install

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
