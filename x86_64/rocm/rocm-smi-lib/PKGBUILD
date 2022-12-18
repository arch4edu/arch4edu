# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: acxz <akashpatel2008 at yahoo dot com>

pkgname=rocm-smi-lib
pkgver=5.4.1
pkgrel=1
pkgdesc='ROCm System Management Interface Library'
arch=('x86_64')
url='https://github.com/RadeonOpenCompute/rocm_smi_lib'
license=('custom:NCSAOSL')
depends=('hsa-rocr' 'python')
makedepends=('cmake' 'doxygen' 'texlive-latexextra')
source=("$pkgname-$pkgver.tar.gz::https://github.com/RadeonOpenCompute/rocm_smi_lib/archive/rocm-$pkgver.tar.gz"
        'missing_string_header.patch::https://patch-diff.githubusercontent.com/raw/RadeonOpenCompute/rocm_smi_lib/pull/107.patch'
)
sha256sums=('40c6471421c18743bb0fe7203ec166c56bf3f7fa25dea62e9455cfe7b3d1659b'
            'f1d66af131833a55bcfcac63e9af7194cc38cb1bb583fb74427e4f0f89719910')
options=(!lto)
_dirname="$(basename "$url")-$(basename "${source[0]}" .tar.gz)"

prepare() {
    cd "$_dirname"
    patch -Np1 -i "$srcdir/missing_string_header.patch"
}

build() {
  cmake \
    -Wno-dev \
    -B build \
    -S "$_dirname" \
    -DCMAKE_INSTALL_PREFIX=/opt/rocm \
    -DCMAKE_BUILD_TYPE=None
  cmake --build build
}

package() {
  DESTDIR="$pkgdir" cmake --install build
  install -Dm644 "$srcdir/$_dirname/License.txt" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
