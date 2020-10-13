# Maintainer Torsten Keßler <t dot kessler at posteo dot de>
pkgname=rocclr
pkgver=3.8.0
pkgrel=1
pkgdesc='Radeon Open Compute Common Language Runtime'
arch=('x86_64')
url='https://github.com/ROCm-Developer-Tools/ROCclr'
license=('MIT')
depends=('mesa' 'comgr' 'hsa-rocr' 'hsakmt-roct' 'rocm-cmake')
makedepends=('cmake')
_opencl='https://github.com/RadeonOpenCompute/ROCm-OpenCL-Runtime'
source=("$pkgname-$pkgver.tar.gz::$url/archive/rocm-$pkgver.tar.gz"
        "$pkgname-opencl-$pkgver.tar.gz::$_opencl/archive/rocm-$pkgver.tar.gz")
sha256sums=('10d8aa6f5af7b51813015da603c4e75edc863c3530793f6ed9769ca345c08ed6'
            '7f75dd1abf3d771d554b0e7b0a7d915ab5f11a74962c92b013ee044a23c1270a')
_dirname="$(basename "$url")-$(basename "${source[0]}" .tar.gz)"

build() {
    cmake -Wno-dev -B build \
	-S "$srcdir/$_dirname" \
	-DCMAKE_INSTALL_PREFIX='/opt/rocm/rocclr' \
        -DOPENCL_DIR="$srcdir/ROCm-OpenCL-Runtime-rocm-$pkgver"

    make -C build
}

package() {
    DESTDIR="$pkgdir" make -C build install
    sed -i "s@$srcdir/build@/opt/rocm/rocclr@" "$pkgdir/opt/rocm/rocclr/lib/cmake/rocclr/ROCclrConfig.cmake"
    install -Dm644 "$_dirname/LICENSE.txt" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
