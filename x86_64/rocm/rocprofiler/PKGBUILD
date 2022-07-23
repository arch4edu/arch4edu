# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: acxz <akashpatel2008 at yahoo dot com>
pkgname=rocprofiler
pkgver=5.2.1
pkgrel=1
pkgdesc="ROC profiler library. Profiling with perf-counters and derived metrics."
arch=('x86_64')
url='https://rocmdocs.amd.com/en/latest/ROCm_Tools/ROCm-Tools.html'
license=('MIT')
depends=('hip' 'python')
makedepends=('cmake' 'python-argparse' 'python-cppheaderparser' 'hsa-rocr')
options=(!staticlibs strip)
_git='https://github.com/ROCm-Developer-Tools/rocprofiler'
_roctracer='https://github.com/ROCm-Developer-Tools/roctracer'
source=("$pkgname-$pkgver.tar.gz::$_git/archive/refs/tags/rocm-$pkgver.tar.gz"
        "$pkgname-roctracer-$pkgver.tar.gz::$_roctracer/archive/refs/tags/rocm-$pkgver.tar.gz")
sha256sums=('c6768ec428590aadfb0e7ef6e22b8dc5ac8ed97babeb56db07f2d5d41cd122e2'
            'e200b5342bdf840960ced6919d4bf42c8f30f8013513f25a2190ee8767667e59')
_dirname="$(basename "$_git")-$(basename "${source[0]}" ".tar.gz")"
_dirtracer="$(basename "$_roctracer")-$(basename "${source[1]}" ".tar.gz")"

build() {
  cmake -B build -Wno-dev \
        -S "$_dirname" \
        -DCMAKE_INSTALL_PREFIX=/opt/rocm \
        -DPROF_API_HEADER_PATH="$srcdir/$_dirtracer/inc/ext"

  make -C build
}

package() {
  DESTDIR="$pkgdir" make -C build install

  install -d "$pkgdir/usr/bin"
  ln -s "/opt/rocm/rocprofiler/bin/rocprof" "$pkgdir/usr/bin/rocprof"

  install -Dm644 "$_dirname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
