# Maintainer: acxz <akashpatel2008 at yahoo dot com>
pkgname=rocprofiler
pkgver=3.7.0
pkgrel=1
pkgdesc="ROC profiler library. Profiling with perf-counters and derived metrics."
arch=('x86_64')
url='https://rocmdocs.amd.com/en/latest/ROCm_Tools/ROCm-Tools.html'
license=('MIT')
depends=('roctracer' 'python')
makedepends=('cmake' 'python-argparse' 'python-cppheaderparser')
options=(!staticlibs strip)
_git='https://github.com/ROCm-Developer-Tools/rocprofiler'
source=("$pkgname-$pkgver.tar.gz::$_git/archive/rocm-$pkgver.tar.gz"
        'add_string_header.patch::https://patch-diff.githubusercontent.com/raw/ROCmSoftwarePlatform/hsa-class/pull/2.patch')
sha256sums=('d3f03bf850cbd86ca9dfe6e6cc6f559d8083b0f3ea4711d8260b232cb6fdd1cc'
            '35c45b367d917b8ecf5d4d738e7761699b115b25530ab5528c8a6a4a49424199')
_dirname="$(basename "$_git")-$(basename "${source[0]}" ".tar.gz")"

prepare() {
    cd "$_dirname"
    patch -Np1 -i "$srcdir/add_string_header.patch"
}

build() {
  cmake -B build -Wno-dev \
        -S "$_dirname" \
        -DCMAKE_INSTALL_PREFIX=/opt/rocm
  
  make -C build
}

package() {
  DESTDIR="$pkgdir" make -C build install

  install -d "$pkgdir/usr/bin"
  ln -s "/opt/rocm/rocprofiler/bin/rocprof" "$pkgdir/usr/bin/rocprof"

  install -Dm644 "$_dirname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
