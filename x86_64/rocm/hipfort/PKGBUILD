# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>

pkgname=hipfort
pkgver=5.4.0
pkgrel=1
pkgdesc='Fortran interfaces for ROCm libraries'
arch=('x86_64')
url='https://rocmsoftwareplatform.github.io/hipfort/'
license=('MIT')
depends=('hip' 'gcc-fortran')
makedepends=('rocm-cmake')
_git='https://github.com/ROCmSoftwarePlatform/hipfort'
source=("$pkgname-$pkgver.tar.gz::$_git/archive/rocm-$pkgver.tar.gz")
sha256sums=('a781bc6d1dbb508a4bd6cc3df931696fac6c6361d4fd35efb12c9a04a72e112c')
options=(!strip)
_dirname="$(basename "$_git")-$(basename "${source[0]}" .tar.gz)"

build() {
    cmake \
        -Wno-dev \
        -B build \
        -S "$_dirname" \
        -DCMAKE_BUILD_TYPE=None \
        -DCMAKE_INSTALL_PREFIX=/opt/rocm/hipfort
    cmake --build build
}

package() {
    DESTDIR="$pkgdir" cmake --install build

    echo "/opt/rocm/$pkgname/lib" > "$pkgname.conf"
    install -Dm644 "$pkgname.conf" "$pkgdir/etc/ld.so.conf.d/$pkgname.conf"

    install -Dm644 "$_dirname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
