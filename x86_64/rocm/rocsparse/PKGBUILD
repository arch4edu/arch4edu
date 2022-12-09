# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: Markus Näther <naetherm@informatik.uni-freiburg.de>
pkgname=rocsparse
pkgver=5.4.0
pkgrel=1
pkgdesc='BLAS for sparse computation on top of ROCm'
arch=('x86_64')
url='https://rocsparse.readthedocs.io/en/master/'
license=('MIT')
depends=('hip' 'rocprim')
makedepends=('rocm-cmake' 'gcc-fortran')
_git='https://github.com/ROCmSoftwarePlatform/rocSPARSE'
source=("$pkgname-$pkgver.tar.gz::$_git/archive/rocm-$pkgver.tar.gz"
        "rocsparse-no-git.patch")
sha256sums=('c8f0e920a8ec15b9ae40564c68191363356cc4d793c16247bb6e11ef5293ed11'
            'bc3cda8fb3e3aad14a2130d9cde7a8c521c2c35448ed69f0873111571d654ad2')
_dirname="$(basename "$_git")-$(basename "${source[0]}" ".tar.gz")"

prepare() {
    cd "$_dirname"
    patch -Np1 -i "$srcdir/rocsparse-no-git.patch"
}

build() {
  # -fcf-protection is not supported by HIP, see
  # https://docs.amd.com/bundle/ROCm-Compiler-Reference-Guide-v5.4/page/Appendix_A.html
  CXXFLAGS="${CXXFLAGS} -fcf-protection=none" \
  cmake \
    -Wno-dev \
    -B build \
    -S "$_dirname" \
    -DCMAKE_BUILD_TYPE=None \
    -DCMAKE_CXX_COMPILER=/opt/rocm/bin/hipcc \
    -DCMAKE_INSTALL_PREFIX=/opt/rocm
  cmake --build build
}

package() {
  DESTDIR="$pkgdir" cmake --install build

  echo '/opt/rocm/rocsparse/lib' > "$pkgname.conf"
  install -Dm644 "$pkgname.conf" "$pkgdir/etc/ld.so.conf.d/$pkgname.conf"

  install -Dm644 "$_dirname/LICENSE.md" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
