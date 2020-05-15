# Maintainer: Jakub Okoński <jakub@okonski.org>
pkgname=rocrand
pkgver=3.3.0
pkgrel=1
pkgdesc="RAND library for HIP programming language"
arch=('x86_64')
url="https://github.com/ROCmSoftwarePlatform/rocRAND"
license=('MIT')
makedepends=("hcc>=$pkgver" 'cmake')
source=("https://github.com/ROCmSoftwarePlatform/rocRAND/archive/rocm-$pkgver.tar.gz")
sha256sums=('ba56556671313b784a1301634df6537f3148426b81bec93b3566e71d22b6f4cc')

build() {
  mkdir -p "$srcdir/build"
  cd "$srcdir/build"

  # build broken with stack protection
  export CFLAGS="$(sed -e 's/-fstack-protector-strong//' <<< "$CFLAGS")"
  export CXXFLAGS="$(sed -e 's/-fstack-protector-strong//' <<< "$CXXFLAGS")"
  export CPPFLAGS="$(sed -e 's/-fstack-protector-strong//' <<< "$CPPFLAGS")"

  cmake -DCMAKE_BUILD_TYPE=Release \
        -DBUILD_TEST=OFF \
        -DCMAKE_CXX_COMPILER=/opt/rocm/hcc/bin/hcc \
        "$srcdir/rocRAND-rocm-$pkgver"

  make
}

package() {
  cd "$srcdir/build"

  make DESTDIR="$pkgdir" install

  install -d "$pkgdir/etc/ld.so.conf.d"
  cat << EOF > "$pkgdir/etc/ld.so.conf.d/rocrand.conf"
/opt/rocm/hiprand/lib
/opt/rocm/rocrand/lib
EOF
}
