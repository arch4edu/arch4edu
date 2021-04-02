# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: acxz <akashpatel at yahoo dot com>
# Contributor: JP-Ellis <josh@jpellis.me>

pkgname=miopen-hip
pkgver=4.1.0
pkgrel=1
pkgdesc="AMD's Machine Intelligence Library (HIP backend)"
arch=('x86_64')
url="https://github.com/ROCmSoftwarePlatform/MIOpen"
license=('MIT')
depends=('rocblas' 'rocm-clang-ocl' 'hip-rocclr')
makedepends=('cmake' 'rocm-cmake' 'miopengemm')
provides=('miopen')
conflicts=('miopen')
source=("$pkgname-$pkgver.tar.gz::$url/archive/rocm-$pkgver.tar.gz")
sha256sums=('068b1bc33f90fe21d3aab5697d2b3b7b930e613c54d6c5ee820768579b2b41ee')
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

  install -Dm644 "$srcdir/$_dirname/LICENSE.txt" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
