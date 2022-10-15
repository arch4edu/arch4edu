# Maintainer Torsten Keßler <t dot kessler at posteo dot de>

pkgname=rocm-dbgapi
pkgver=5.3.0
pkgrel=1
pkgdesc="Support library necessary for a debugger of AMD's GPUs"
arch=('x86_64')
url='https://github.com/ROCm-Developer-Tools/ROCdbgapi'
license=('MIT')
depends=('comgr' 'hsa-rocr')
makedepends=('rocm-cmake' 'git' 'doxygen' 'texlive-latexextra')
source=("$pkgname-$pkgver.tar.gz::$url/archive/rocm-$pkgver.tar.gz")
sha256sums=('afffec78e34fe70952cd41efc3d7ba8f64e43acb2ad20aa35c9b8b591bed48ca')
_dirname=$(basename "$url")-$(basename "${source[0]}" ".tar.gz")

build() {
    cmake \
      -Wno-dev \
      -B build \
      -S "$_dirname" \
      -DCMAKE_INSTALL_PREFIX=/opt/rocm
    cmake --build build --target doc all
}

package() {
    DESTDIR="$pkgdir" cmake --install build
    install -Dm644 "$srcdir/$_dirname/LICENSE.txt" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
