# Maintainer: Markus Näther <naetherm@informatik.uni-freiburg.de>
pkgname=rocsparse
pkgver=3.7.0
pkgrel=1
pkgdesc='BLAS for sparse computation on top of ROCm'
arch=('x86_64')
url='https://rocmdocs.amd.com/en/latest/ROCm_Libraries/ROCm_Libraries.html#rocsparse'
license=('MIT')
depends=('hip-rocclr' 'rocprim')
makedepends=('cmake' 'git' 'gcc-fortran')
_git='https://github.com/ROCmSoftwarePlatform/rocSPARSE'
source=("$pkgname-$pkgver.tar.gz::$_git/archive/rocm-$pkgver.tar.gz"
        'remove-boz-literals.patch::https://patch-diff.githubusercontent.com/raw/ROCmSoftwarePlatform/rocSPARSE/pull/210.patch')
sha256sums=('db561ae5e8ee117f7c539a9ef6ee49c13b82ba9f702b22c76e741cca245386a9'
            'bb34dd66788f1456cf2a711ec537441933b89ffde080de6f941bdfe71585c445')
_dirname="$(basename "$_git")-$(basename "${source[0]}" ".tar.gz")"

prepare() {
    cd "$_dirname"
    patch -Np1 -i "$srcdir/remove-boz-literals.patch"
}

build() {
  CXX=/opt/rocm/hip/bin/hipcc \
  cmake -Wno-dev -S "$_dirname" \
        -DCMAKE_INSTALL_PREFIX=/opt/rocm \
        -Drocprim_DIR=/opt/rocm/rocprim/rocprim/lib/cmake/rocprim \
        -DBUILD_CLIENTS_SAMPLES=OFF
  make
}

package() {
  DESTDIR="$pkgdir" make install

  install -Dm644 /dev/stdin "$pkgdir/etc/ld.so.conf.d/rocsparse.conf" <<EOF
/opt/rocm/rocsparse/lib
EOF
  install -Dm644 "$_dirname/LICENSE.md" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
