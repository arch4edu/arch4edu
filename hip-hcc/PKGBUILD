# Maintainer: acxz <akashpatel2008 at yahoo dot com>
pkgname=hip-hcc
pkgver=3.3.0
pkgrel=6
pkgdesc="Heterogeneous Interface for Portability ROCm"
arch=('x86_64')
url='https://rocmdocs.amd.com/en/latest/Installation_Guide/HIP.html'
license=('MIT')
depends=('hsa-rocr' 'comgr')
makedepends=('libelf' 'cmake' 'python' 'hcc' 'git')
provides=('hip')
conflicts=('hip')
_git='https://github.com/ROCm-Developer-Tools/HIP'
source=("$pkgname-$pkgver.tar.gz::$_git/archive/rocm-$pkgver.tar.gz")
sha256sums=('8ae7cf4134975c7a36e0c72a5e041694935f38c2d7df58f4ad55e9a23b7b875c')

prepare() {
  cd "$srcdir/HIP-rocm-$pkgver"

  # override __hcc_workweek__
  # https://github.com/rocm-arch/rocm-arch/issues/68#issuecomment-604272120
  sed -i 's/__hcc_workweek__/99999/g' $(grep __hcc_workweek__ . -rIl)
}

build() {
  mkdir -p "$srcdir/build"
  cd "$srcdir/build"

  cmake -DCMAKE_INSTALL_PREFIX=/opt/rocm/hip \
        -DHIP_COMPILER=hcc \
        "$srcdir/HIP-rocm-$pkgver"
  make
}

package() {
  cd "$srcdir/build"

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
  install -Dm644 "$srcdir/HIP-rocm-$pkgver/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
