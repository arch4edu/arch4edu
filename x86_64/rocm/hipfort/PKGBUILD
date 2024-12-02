# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>

pkgname=hipfort
pkgver=6.2.4
pkgrel=1
pkgdesc='Fortran interfaces for ROCm libraries'
arch=('x86_64')
url='https://rocm.docs.amd.com/projects/hipfort/en/latest/'
license=('MIT')
depends=('hip-runtime-amd' 'gcc-fortran')
makedepends=('rocm-cmake')
_git='https://github.com/ROCmSoftwarePlatform/hipfort'
source=("$pkgname-$pkgver.tar.gz::$_git/archive/rocm-$pkgver.tar.gz")
sha256sums=('32daa4ee52c2d44790bff7a7ddde9d572e4785b2f54766a5e45d10228da0534b')
options=(!strip)
_dirname="$(basename "$_git")-$(basename "${source[0]}" .tar.gz)"

build() {
    cmake \
        -Wno-dev \
        -B build \
        -S "$_dirname" \
        -DCMAKE_BUILD_TYPE=None \
        -DCMAKE_INSTALL_PREFIX=/opt/rocm \
        -DBUILD_SHARED_LIBS=ON
    cmake --build build
}

package() {
    DESTDIR="$pkgdir" cmake --install build

    install -Dm644 "$_dirname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
