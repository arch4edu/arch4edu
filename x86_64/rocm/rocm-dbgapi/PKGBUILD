# Maintainer Torsten Keßler <t dot kessler at posteo dot de>

pkgname=rocm-dbgapi
pkgver=5.2.3
pkgrel=1
pkgdesc="Support library necessary for a debugger of AMD's GPUs"
arch=('x86_64')
url='https://github.com/ROCm-Developer-Tools/ROCdbgapi'
license=('MIT')
depends=('comgr' 'hsa-rocr')
makedepends=('cmake' 'rocm-cmake' 'git' 'doxygen' 'texlive-latexextra')
source=("$pkgname-$pkgver.tar.gz::$url/archive/rocm-$pkgver.tar.gz")
sha256sums=('17925d23f614ecb2b40dffe5e14535cba380d4f489ea1a027762c356be9fbc2b')
_dirname=$(basename "$url")-$(basename "${source[0]}" ".tar.gz")

build() {
    cmake   -Wno-dev -B build \
            -S "$_dirname" \
            -DCMAKE_INSTALL_PREFIX=/opt/rocm

    make -C build doc all
}

package() {
    DESTDIR="$pkgdir" make -C build install
    install -Dm644 "$srcdir/$_dirname/LICENSE.txt" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
