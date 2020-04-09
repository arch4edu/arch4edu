# Maintainer: acxz <akashpatel2008 at yahoo dot com>
pkgname=rocprofiler
pkgver=3.3.0
pkgrel=1
pkgdesc="ROC profiler library. Profiling with perf-counters and derived metrics."
arch=('x86_64')
url="https://github.com/ROCm-Developer-Tools/rocprofiler"
license=('MIT')
depends=('hsa-rocr' 'python' 'python-argparse' 'python-cppheaderparser')
makedepends=('cmake')
options=(!staticlibs strip)
source=("rocprofiler-roc-$pkgver.tar.gz::https://github.com/ROCm-Developer-Tools/rocprofiler/archive/roc-$pkgver.tar.gz")
sha256sums=('dccdcf95f5d237866cb9bd57492457ebed246d5fa75cb8e976631a1c9c5449aa')

build() {
  mkdir -p "$srcdir/build"
  cd "$srcdir/build"

  cmake -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_PREFIX=/opt/rocm \
        "$srcdir/rocprofiler-roc-$pkgver"
  make
}

package() {
  cd "$srcdir/build"

  make DESTDIR="$pkgdir" install

  # add links
  install -d "$pkgdir/usr/bin"
  local _fn
  for _fn in rocprofiler; do
    ln -s "/opt/rocm/rocprofiler/bin/$_fn" "$pkgdir/usr/bin/$_fn"
  done
}
