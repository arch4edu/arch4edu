# Maintainer Torsten Keßler <t dot kessler at posteo dot de>

pkgname=hipfort
pkgver=5.1.3
pkgrel=1
pkgdesc='Fortran interfaces for ROCm libraries'
arch=('x86_64')
url='https://rocmsoftwareplatform.github.io/hipfort/'
license=('MIT')
depends=('hip' 'gcc-fortran')
makedepends=('cmake' 'rocm-cmake' 'git')
_git='https://github.com/ROCmSoftwarePlatform/hipfort'
source=("$pkgname-$pkgver.tar.gz::$_git/archive/rocm-$pkgver.tar.gz")
sha256sums=('8f8849d8d0972366bafa41be35cf6a7a59480ed584d1ddff39768cb14247e9d4')
options=(!strip)
_dirname="$(basename "$_git")-$(basename "${source[0]}" .tar.gz)"

build() {
    cmake   -B build -Wno-dev \
            -S "$_dirname" \
            -DCMAKE_INSTALL_PREFIX=/opt/rocm/hipfort

    make -C build
}

package() {
    DESTDIR="$pkgdir" make -C build install

    install -Dm644 /dev/stdin "$pkgdir/etc/ld.so.conf.d/$pkgname.conf" <<-EOF
        /opt/rocm/$pkgname/lib
EOF
    install -Dm644 "$_dirname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
