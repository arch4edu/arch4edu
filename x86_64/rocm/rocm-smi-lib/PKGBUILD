# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: acxz <akashpatel2008 at yahoo dot com>

pkgname=rocm-smi-lib
pkgver=5.3.0
pkgrel=1
pkgdesc='ROCm System Management Interface Library'
arch=('x86_64')
url='https://github.com/RadeonOpenCompute/rocm_smi_lib'
license=('custom:NCSAOSL')
depends=('hsa-rocr')
makedepends=('cmake' 'doxygen' 'texlive-latexextra')
source=("$pkgname-$pkgver.tar.gz::https://github.com/RadeonOpenCompute/rocm_smi_lib/archive/rocm-$pkgver.tar.gz"
        'missing_string_header.patch::https://patch-diff.githubusercontent.com/raw/RadeonOpenCompute/rocm_smi_lib/pull/107.patch'
)
sha256sums=('8f72ad825a021d5199fb73726b4975f20682beb966e0ec31b53132bcd56c5408'
            'f1d66af131833a55bcfcac63e9af7194cc38cb1bb583fb74427e4f0f89719910')
options=(!lto)
_dirname="$(basename "$url")-$(basename "${source[0]}" .tar.gz)"

prepare() {
    cd "$_dirname"
    patch -Np1 -i "$srcdir/missing_string_header.patch"
}

build() {
  # build type Release fixes warnings regarding FORTIFY_SOURCE
  cmake \
    -Wno-dev \
    -B build \
    -S "$_dirname" \
    -DCMAKE_INSTALL_PREFIX=/opt/rocm \
    -DCMAKE_BUILD_TYPE=Release
  cmake --build build
}

package() {
  DESTDIR="$pkgdir" cmake --install build
  install -Dm644 "$srcdir/$_dirname/License.txt" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
