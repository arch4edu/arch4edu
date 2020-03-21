# Maintainer: acxz <akashpatel2008 at yahoo dot com>
# Contributor: Jakub Okoński <jakub@okonski.org>
pkgname=roct-thunk-interface
pkgver=3.1.0
pkgrel=1
pkgdesc="Radeon Open Compute Thunk Interface"
arch=('x86_64')
url="https://github.com/RadeonOpenCompute/ROCT-Thunk-Interface"
license=('MIT')
depends=('numactl' 'pciutils')
makedepends=('cmake')
source=("https://github.com/RadeonOpenCompute/ROCT-Thunk-Interface/archive/roc-$pkgver.tar.gz")
sha256sums=('b08176b5f4af39d0160990f9f1dea5d27974f9282f544140b4a41d19446fe570')

build() {
  mkdir -p "$srcdir/build"
  cd "$srcdir/build"

  cmake -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_PREFIX=/opt/rocm \
        "$srcdir/ROCT-Thunk-Interface-roc-$pkgver"
  make all build-dev
}

package() {
  cd "$srcdir/build"

  make DESTDIR="$pkgdir" install install-dev

  install -d "$pkgdir/etc/ld.so.conf.d"
  cat << EOF > "$pkgdir/etc/ld.so.conf.d/roct-thunk-interface.conf"
/opt/rocm/lib
EOF
}
