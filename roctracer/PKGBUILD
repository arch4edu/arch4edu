# Maintainer: acxz <akashpatel2008 at yahoo dot com>
pkgname=roctracer
pkgver=3.5.0
pkgrel=1
pkgdesc="ROCm Tracer Callback/Activity Library for Performance tracing AMD GPU's"
arch=('x86_64')
url='https://rocmdocs.amd.com/en/latest/ROCm_Tools/ROCm-Tools.html#amd-rocm-roctracer'
license=('MIT')
depends=('hsa-rocr')
makedepends=('cmake' 'git' 'python' 'python-argparse' 'python-cppheaderparser')
options=(!staticlibs strip)
_git='https://github.com/ROCm-Developer-Tools/roctracer'
source=("roctracer-rocm-$pkgver.tar.gz::$_git/archive/rocm-$pkgver.tar.gz"
        'add_string_header.patch')
sha256sums=('7af5326c9ca695642b4265232ec12864a61fd6b6056aa7c4ecd9e19c817f209e'
            '78282e835e495d9499b5e4a759772b80443122390022f4560a500d11e9d6bf0d')

build() {
  mkdir -p build
  cd build

  cmake -DCMAKE_INSTALL_PREFIX=/opt/rocm \
        "$srcdir/roctracer-rocm-$pkgver"
  
  cd "$srcdir/roctracer-rocm-$pkgver"
  patch -Np1 -i "$srcdir/add_string_header.patch"
 
  cd "$srcdir/build"
  make
}

package() {
  cd build

  make DESTDIR="$pkgdir" install

  install -Dm644 "$srcdir/roctracer-rocm-$pkgver/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
