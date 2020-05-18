# Maintainer: Jakub Okoński <jakub@okonski.org>
pkgname=rocrand
pkgver=3.3.0
pkgrel=2
pkgdesc='Pseudo-random and quasi-random number generator on ROCm'
arch=('x86_64')
url='https://rocmdocs.amd.com/en/latest/ROCm_Libraries/ROCm_Libraries.html#rocrand'
license=('MIT')
depends=('hip-hcc')
makedepends=('hcc' 'cmake' 'git')
_git='https://github.com/ROCmSoftwarePlatform/rocRAND'
source=("$pkgname-$pkgver.tar.gz::$_git/archive/rocm-$pkgver.tar.gz")
sha256sums=('ba56556671313b784a1301634df6537f3148426b81bec93b3566e71d22b6f4cc')

build() {
  mkdir -p build
  cd build

  # build broken with stack protection
  export CFLAGS="$(sed -e 's/-fstack-protector-strong//' <<< "$CFLAGS")"
  export CXXFLAGS="$(sed -e 's/-fstack-protector-strong//' <<< "$CXXFLAGS")"
  export CPPFLAGS="$(sed -e 's/-fstack-protector-strong//' <<< "$CPPFLAGS")"

  CXX=/opt/rocm/hcc/bin/hcc \
  cmake -DCMAKE_INSTALL_PREFIX=/opt/rocm/rocrand \
        -Damd_comgr_DIR=/opt/rocm/lib/cmake/amd_comgr \
        -DBUILD_TEST=OFF \
        "$srcdir/rocRAND-rocm-$pkgver"
  make
}

package() {
  cd "$srcdir/build"

  make DESTDIR="$pkgdir" install

  install -Dm644 /dev/stdin "$pkgdir/etc/ld.so.conf.d/rocrand.conf" << EOF
/opt/rocm/hiprand/lib
/opt/rocm/rocrand/lib
EOF
  install -Dm644 "$srcdir/rocRAND-rocm-$pkgver/LICENSE.txt" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
