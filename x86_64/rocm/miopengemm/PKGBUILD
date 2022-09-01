# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: acxz <akashpatel2008 at yahoo dot com>
# Contributor: Jakub Okoński <jakub@okonski.org>
pkgname=miopengemm
pkgver=5.2.3
pkgrel=1
pkgdesc="An OpenCL GEMM kernel generator"
arch=('x86_64')
url="https://github.com/ROCmSoftwarePlatform/MIOpenGEMM"
license=('MIT')
depends=('ocl-icd')
makedepends=('opencl-headers' 'cmake' 'rocm-cmake' 'texlive-latexextra')
source=("$pkgname-$pkgver.tar.gz::$url/archive/rocm-$pkgver.tar.gz"
        "fix-gcc11-build.patch::https://patch-diff.githubusercontent.com/raw/ROCmSoftwarePlatform/MIOpenGEMM/pull/46.patch")
sha256sums=('de9eecf39e6620be1511923e990101e64c63c2f56d8491c8bf9ffd1033709c00'
            'SKIP')
_dirname="$(basename "$url")-$(basename "${source[0]}" ".tar.gz")"

prepare() {
    cd "$_dirname"
    patch -Np1 -i "${srcdir}/fix-gcc11-build.patch"
}

build() {
  cmake -S "$_dirname" -Wno-dev \
        -DCMAKE_INSTALL_PREFIX=/opt/rocm
  make
}

package() {
  make DESTDIR="$pkgdir" install

  install -Dm644 "$srcdir/$_dirname/LICENSE.txt" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
