# Maintainer: acxz <akashpatel2008 at yahoo dot com>
pkgname=rocprofiler
pkgver=3.5.0
pkgrel=3
pkgdesc="ROC profiler library. Profiling with perf-counters and derived metrics."
arch=('x86_64')
url='https://rocmdocs.amd.com/en/latest/ROCm_Tools/ROCm-Tools.html'
license=('MIT')
depends=('roctracer' 'python')
makedepends=('cmake' 'python-argparse' 'python-cppheaderparser')
options=(!staticlibs strip)
_git='https://github.com/ROCm-Developer-Tools/rocprofiler'
source=("$pkgname-$pkgver.tar.gz::$_git/archive/rocm-$pkgver.tar.gz"
        'add_string_header.patch')
sha256sums=('c42548dd467b7138be94ad68c715254eb56a9d3b670ccf993c43cd4d43659937'
            '40264623a8431f63662137963852e1e6c025e1960212cdf4b08ce00a370b7cc4')

prepare(){
    cd "rocprofiler-rocm-$pkgver"
    patch -Np1 -i ../add_string_header.patch
}

build() {
  cmake -B build -Wno-dev \
        -DCMAKE_INSTALL_PREFIX=/opt/rocm \
        "$srcdir/rocprofiler-rocm-$pkgver"
  make -C build
}

package() {
  DESTDIR="$pkgdir" make -C build install

  install -d "$pkgdir/usr/bin"
  ln -s "/opt/rocm/rocprofiler/bin/rocprof" "$pkgdir/usr/bin/rocprof"

  install -Dm644 "$srcdir/rocprofiler-rocm-$pkgver/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
