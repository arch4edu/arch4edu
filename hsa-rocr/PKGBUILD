# Maintainer: acxz <akashpatel2008 at yahoo dot com>
# Contributor: Olaf Leidinger <oleid@mescharet.de>
# Contributor: Bruno Filipe <bmilreu@gmail.com>
# Contributor: Jakub Okoński <jakub@okonski.org>
# Contributor: Ranieri Althoff <ranisalt+aur at gmail.com>

pkgname=hsa-rocr
pkgver=3.3.0
pkgrel=2
pkgdesc='ROCm Platform Runtime: ROCr a HPC market enhanced HSA based runtime'
arch=('x86_64')
url='https://github.com/RadeonOpenCompute/ROCR-Runtime'
license=('custom:NCSAOSL')
makedepends=('cmake' 'libelf' "hsakmt-roct")
provides=("rocr-runtime=$pkgver")
replaces=('rocr-runtime')
conflicts=('rocr-runtime')
source=("$url/archive/rocm-$pkgver.tar.gz")
sha256sums=('fa2d2d1f8a61d8a6952d377cf288d78c61776c3c2a666f163cafc3aa19ab0b61')
_dirname="$(basename "$url")-$(basename "${source[0]}" .tar.gz)"

build() {
  cmake -DCMAKE_INSTALL_PREFIX=/opt/rocm \
        -DHSAKMT_INC_PATH=/opt/rocm/include \
        -DHSAKMT_LIB_PATH=/opt/rocm/lib \
        "$_dirname/src"
  make
}

package() {
  make DESTDIR="$pkgdir" install

  install -Dm644 "$_dirname/LICENSE.txt" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
  install -Dm644 /dev/stdin "$pkgdir/etc/ld.so.conf.d/rocm-runtime.conf" <<-EOF
    /opt/rocm/lib
    /opt/rocm/hsa/lib
EOF
}
