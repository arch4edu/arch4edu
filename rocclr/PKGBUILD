# Maintainer Torsten Keßler <t dot kessler at posteo dot de>
pkgname=rocclr
pkgver=3.5.0
pkgrel=1
pkgdesc='Radeon Open Compute Common Language Runtime'
arch=('x86_64')
url='https://github.com/ROCm-Developer-Tools/ROCclr'
license=('unknown')
depends=('mesa' 'comgr' 'rocm-cmake')
makedepends=('git' 'cmake')
source=("$pkgname-$pkgver.tar.gz::$url/archive/roc-$pkgver.tar.gz"
        "$pkgname-opencl-$pkgver.tar.gz::https://github.com/RadeonOpenCompute/ROCm-OpenCL-Runtime/archive/roc-$pkgver.tar.gz")
sha256sums=('87c1ee9f02b8aa487b628c543f058198767c474cec3d21700596a73c028959e1'
            '511b617d5192f2d4893603c1a02402b2ac9556e9806ff09dd2a91d398abf39a0')

build() {
    mkdir -p build
    cd build
    cmake "$srcdir/ROCclr-roc-$pkgver" \
        -DCMAKE_INSTALL_PREFIX='/opt/rocm/rocclr' \
        -DOPENCL_DIR="$srcdir/ROCm-OpenCL-Runtime-roc-$pkgver"

    make
}

package() {
    make -C build DESTDIR="$pkgdir/" install

    sed -i "s@$srcdir/build/libamdrocclr_static.a@/opt/rocm/rocclr/lib/libamdrocclr_static.a@" \
        "$srcdir/build/amdrocclr_staticTargets.cmake"
    install -Dm644 "$srcdir/build/amdrocclr_staticTargets.cmake" \
        "$pkgdir/opt/rocm/rocclr/lib/amdrocclr_staticTargets.cmake"
}
