# Maintainer: acxz <akashpatel2008 at yahoo dot com>
pkgname=roctracer
pkgver=3.5.0
pkgrel=2
pkgdesc="ROCm Tracer Callback/Activity Library for Performance tracing AMD GPU's"
arch=('x86_64')
url='https://rocmdocs.amd.com/en/latest/ROCm_Tools/ROCm-Tools.html#amd-rocm-roctracer'
license=('MIT')
depends=('hip-rocclr')
makedepends=('cmake' 'git' 'python' 'python-argparse' 'python-cppheaderparser' 'python-ply')
options=(!staticlibs strip)
_git='https://github.com/ROCm-Developer-Tools/roctracer'
source=("roctracer-rocm-$pkgver.tar.gz::$_git/archive/rocm-$pkgver.tar.gz"
        'add_string_header.patch::https://patch-diff.githubusercontent.com/raw/ROCmSoftwarePlatform/hsa-class/pull/2.patch')
sha256sums=('7af5326c9ca695642b4265232ec12864a61fd6b6056aa7c4ecd9e19c817f209e'
            '35c45b367d917b8ecf5d4d738e7761699b115b25530ab5528c8a6a4a49424199')

build() {
  cmake -B build -Wno-dev \
        -DCMAKE_INSTALL_PREFIX=/opt/rocm \
        -DHIP_VDI=1 \
        "$srcdir/roctracer-rocm-$pkgver"
  
  cd "$srcdir/roctracer-rocm-$pkgver/test/hsa"
  patch -Np1 -i "$srcdir/add_string_header.patch"
 
  cd "$srcdir/build"
  make
}

package() {
  DESTDIR="$pkgdir" make -C build install

  install -Dm644 "$srcdir/roctracer-rocm-$pkgver/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
