# Maintainer: acxz <akashpatel2008 at yahoo dot com>
pkgname=hip-hcc
pkgver=3.1.0
pkgrel=2
pkgdesc="Heterogeneous Interface for Portability ROCm"
arch=('x86_64')
url="https://github.com/ROCm-Developer-Tools/HIP"
license=('MIT')
makedepends=('libelf' 'cmake' 'hcc' 'rocm-comgr')
provides=('hip')
conflicts=('hip')
source=("https://github.com/ROCm-Developer-Tools/HIP/archive/roc-$pkgver.tar.gz")
sha256sums=('3e7b7ef508f4c0d34756104936bc25eaffe419415013c93da72244aac199ae91')

build() {
  mkdir -p "$srcdir/build"
  cd "$srcdir/build"

  cmake -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_PREFIX=/opt/rocm/hip \
        -DHIP_COMPILER=hcc \
        "$srcdir/HIP-roc-$pkgver"
  make
}

package() {
  cd "$srcdir/build"

  make DESTDIR="$pkgdir" install

  install -d "$pkgdir/etc/ld.so.conf.d"
  cat << EOF > "$pkgdir/etc/ld.so.conf.d/hip.conf"
/opt/rocm/hip/lib
EOF
}
