# Maintainer: acxz <akashpatel2008 at yahoo dot com>
# Contributor: Jakub Okoński <jakub@okonski.org>
pkgname=rocr-runtime
pkgver=3.1.0
pkgrel=1
pkgdesc="ROCm Platform Runtime: ROCr a HPC market enhanced HSA based runtime"
arch=('x86_64')
url="https://github.com/RadeonOpenCompute/ROCR-Runtime"
license=('custom:NCSAOSL')
makedepends=('cmake' 'libelf' 'roct-thunk-interface')
source=("https://github.com/RadeonOpenCompute/ROCR-Runtime/archive/roc-$pkgver.tar.gz")
sha256sums=('b162464ef87ce39518e59ef8406d6b897aa7a930795c586829614ed87aa1c2ce')

build() {
  mkdir -p "$srcdir/build"
  cd "$srcdir/build"

  cmake -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_PREFIX=/opt/rocm \
        -DHSAKMT_INC_PATH=/opt/rocm/include \
        -DHSAKMT_LIB_PATH=/opt/rocm/lib \
        "$srcdir/ROCR-Runtime-roc-$pkgver/src"
  make
}

package() {
  cd "$srcdir/build"

  make DESTDIR="$pkgdir" install

  install -d "$pkgdir/etc/ld.so.conf.d"
  cat << EOF > "$pkgdir/etc/ld.so.conf.d/rocm-runtime.conf"
/opt/rocm/lib
/opt/rocm/hsa/lib
EOF
}
