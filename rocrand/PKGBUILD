# Maintainer: Jakub Okoński <jakub@okonski.org>
pkgname=rocrand
pkgver=3.10.0
pkgrel=1
pkgdesc='Pseudo-random and quasi-random number generator on ROCm'
arch=('x86_64')
url='https://rocmdocs.amd.com/en/latest/ROCm_Libraries/ROCm_Libraries.html#rocrand'
license=('MIT')
depends=('hip-rocclr')
makedepends=('cmake' 'git')
_git='https://github.com/ROCmSoftwarePlatform/rocRAND'
source=("$pkgname-$pkgver.tar.gz::$_git/archive/rocm-$pkgver.tar.gz")
sha256sums=('f55e2b49b4dfd887e46eea049f3359ae03c60bae366ffc979667d364205bc99c')
_dirname="$(basename "$_git")-$(basename "${source[0]}" ".tar.gz")"

build() {
  CXX=/opt/rocm/hip/bin/hipcc \
  cmake -Wno-dev -S "$_dirname" \
        -DCMAKE_INSTALL_PREFIX=/opt/rocm \
        -Damd_comgr_DIR=/opt/rocm/lib/cmake/amd_comgr \
        -DBUILD_TEST=OFF
  make
}

package() {
  DESTDIR="$pkgdir" make install

  install -Dm644 /dev/stdin "$pkgdir/etc/ld.so.conf.d/rocrand.conf" << EOF
/opt/rocm/hiprand/lib
/opt/rocm/rocrand/lib
EOF
  install -Dm644 "$_dirname/LICENSE.txt" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"

  # Some packages search for {roc,hip}rand includes in /opt/rocm/include/{roc,hip}rand
  install -d "$pkgdir/opt/rocm/include"
  ln -s "/opt/rocm/hiprand/include/" "$pkgdir/opt/rocm/include/hiprand"
  ln -s "/opt/rocm/rocrand/include/" "$pkgdir/opt/rocm/include/rocrand"
}
