# Maintainer: acxz <akashpatel2008 at yahoo dot com>
pkgname=rocm-debug-agent
pkgver=3.8.0
pkgrel=1
pkgdesc="ROCr Debug Agent Library"
arch=('x86_64')
url="https://github.com/ROCm-Developer-Tools/rocr_debug_agent"
license=('custom:NCSAOSL')
depends=('hip-rocclr' 'rocm-dbgapi' 'glibc')
makedepends=('cmake' 'git')
options=(!staticlibs strip)
source=("$pkgname-$pkgver.tar.gz::$url/archive/rocm-$pkgver.tar.gz")
sha256sums=('55243331ac4b0d90e88882eb29fd06fad354e278f8a34ac7f0680b2c895ca2ac')
_dirname="$(basename "$url")-$(basename "${source[0]}" ".tar.gz")"

build() {
  cmake -Wno-dev -S "$_dirname" \
        -DCMAKE_INSTALL_PREFIX=/opt/rocm/rocr_debug_agent
  make
}

package() {
  make DESTDIR="$pkgdir" install
}
