# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: acxz <akashpatel2008 at yahoo dot com>
pkgname=rocprofiler
pkgver=5.3.0
pkgrel=1
pkgdesc="ROC profiler library. Profiling with perf-counters and derived metrics."
arch=('x86_64')
url='https://rocmdocs.amd.com/en/latest/ROCm_Tools/ROCm-Tools.html'
license=('MIT')
depends=('hip' 'python' 'hsa-amd-aqlprofile')
makedepends=('cmake' 'python-argparse' 'python-cppheaderparser' 'hsa-rocr')
_git='https://github.com/ROCm-Developer-Tools/rocprofiler'
_roctracer='https://github.com/ROCm-Developer-Tools/roctracer'
source=("$pkgname-$pkgver.tar.gz::$_git/archive/refs/tags/rocm-$pkgver.tar.gz"
        "$pkgname-roctracer-$pkgver.tar.gz::$_roctracer/archive/refs/tags/rocm-$pkgver.tar.gz")
sha256sums=('b0905a329dc1c97a362b951f3f8ef5da9d171cabb001ed4253bd59a2742e7d39'
            '36f1da60863a113bb9fe2957949c661f00a702e249bb0523cda1fb755c053808')
_dirname="$(basename "$_git")-$(basename "${source[0]}" ".tar.gz")"
_dirtracer="$(basename "$_roctracer")-$(basename "${source[1]}" ".tar.gz")"

build() {
  cmake \
    -Wno-dev \
    -B build \
    -S "$_dirname" \
    -DCMAKE_INSTALL_PREFIX=/opt/rocm \
    -DPROF_API_HEADER_PATH="$srcdir/$_dirtracer/inc/ext"
  cmake --build build
}

package() {
  DESTDIR="$pkgdir" cmake --install build

  install -Dm644 "$_dirname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
