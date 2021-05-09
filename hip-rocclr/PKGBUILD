# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: acxz <akashpatel2008 at yahoo dot com>
pkgname=hip-rocclr
pkgver=4.1.1
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
sha256sums=('4dbdbcd79e8803387790cba7ea94f28fd312a60e6704361f43b3241d2afe0f45'
            'c6358b4dfac658c0a27a3425ace455d951cd26be827dd7751c28cb83dc84b67d')
_dirname="$(basename "$_git")-$(basename "${source[0]}" ".tar.gz")"

prepare() {
    cd "$_dirname"
    patch -Np1 -i "$srcdir/amdgpu-targets.patch"
}

build() {
  CXXFLAGS="$CXXFLAGS -isystem /opt/rocm/include/compiler/lib/include -isystem /opt/rocm/include/elf" \
  cmake -B build -Wno-dev \
        -S "$_dirname" \
        -DCMAKE_INSTALL_PREFIX=/opt/rocm \
        -DHIP_COMPILER=clang \
        -DHIP_PLATFORM=rocclr \
        -D__HIP_ENABLE_PCH=OFF
  make -C build
}

package() {
  DESTDIR="$pkgdir" make -C build install

  # add links (hipconfig is for rocblas with tensile)
  install -d "$pkgdir/usr/bin"
  local _fn
  for _fn in hipcc hipconfig; do
    ln -s "/opt/rocm/bin/$_fn" "$pkgdir/usr/bin/$_fn"
  done

  install -Dm644 /dev/stdin "$pkgdir/etc/ld.so.conf.d/hip.conf" <<EOF
/opt/rocm/lib
EOF
  install -Dm644 "$srcdir/HIP-rocm-$pkgver/LICENSE.txt" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
