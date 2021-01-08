# Maintainer: acxz <akashpatel at yahoo dot com>
# Contributor: JP-Ellis <josh@jpellis.me>

pkgname=miopen-hip
pkgver=4.0.0
pkgrel=3
pkgdesc="AMD's Machine Intelligence Library (HIP backend)"
arch=('x86_64')
url="https://github.com/ROCmSoftwarePlatform/MIOpen"
license=('custom:NCSAOSL')
depends=('rocblas' 'llvm-amdgpu' 'rocm-clang-ocl' 'hip')
makedepends=('cmake' 'rocm-cmake' 'miopengemm' 'rocminfo')
provides=('miopen')
conflicts=('miopen')
source=("$pkgname-$pkgver.tar.gz::$url/archive/rocm-$pkgver.tar.gz")
sha256sums=('84c6c17be9c1a9cd0d3a2af283433f64b07a4b9941349f498e40fed82fb205a6')
_dirname="$(basename "$url")-$(basename "${source[0]}" .tar.gz)"

build() {
  cd "$_dirname"
  cmake -P install_deps.cmake \
        --minimum --prefix "$srcdir/deps"

  CXX=/opt/rocm/llvm/bin/clang++ \
  cmake -B build -Wno-dev \
        -DMIOPEN_BACKEND=HIP \
        -DCMAKE_INSTALL_PREFIX=/opt/rocm \
        -DCMAKE_PREFIX_PATH="$srcdir/deps"

  make -C build
}

package() {
  DESTDIR="$pkgdir" make -C "$_dirname/build" install

  install -d "$pkgdir/etc/ld.so.conf.d"
  cat << EOF > "$pkgdir/etc/ld.so.conf.d/miopen.conf"
/opt/rocm/miopen/lib
EOF
}
