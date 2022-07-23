# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: acxz <akashpatel2008 at yahoo dot com>

pkgname=rocm-smi-lib
pkgver=5.2.1
pkgrel=1
pkgdesc='ROCm System Management Interface Library'
arch=('x86_64')
url="https://github.com/RadeonOpenCompute/rocm_smi_lib"
license=('custom:NCSAOSL')
depends=('hsa-rocr')
provides=("rocm-smi-lib64=$pkgver")
replaces=('rocm-smi-lib64')
conflicts=('rocm-smi-lib64')
makedepends=('cmake' 'doxygen' 'texlive-latexextra')
source=("$pkgname-$pkgver.tar.gz::https://github.com/RadeonOpenCompute/rocm_smi_lib/archive/rocm-$pkgver.tar.gz"
        'missing_string_header.patch::https://patch-diff.githubusercontent.com/raw/RadeonOpenCompute/rocm_smi_lib/pull/107.patch'
)
sha256sums=('07ad3be6f8c7d3f0a1b8b79950cd7839fb82972cef373dccffdbda32a3aca760'
            'f1d66af131833a55bcfcac63e9af7194cc38cb1bb583fb74427e4f0f89719910')
options=(!lto)
_dirname="$(basename "$url")-$(basename "${source[0]}" .tar.gz)"

prepare() {
    cd "$_dirname"
    patch -Np1 -i "$srcdir/missing_string_header.patch"
}

build() {
  # build type Release fixes warnings regarding FORTIFY_SOURCE
  cmake -DCMAKE_INSTALL_PREFIX=/opt/rocm \
        -DCMAKE_BUILD_TYPE=Release \
        -S "$_dirname" \
        -B build
  make -C build
}

package() {
  DESTDIR="$pkgdir" make -C build install
  install -Dm644 "$srcdir/$_dirname/License.txt" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
