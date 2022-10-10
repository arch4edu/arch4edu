# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: Jakub Okoński <jakub@okonski.org>
pkgname=rocrand
pkgver=5.3.0
pkgrel=1
pkgdesc='Pseudo-random and quasi-random number generator on ROCm'
arch=('x86_64')
url='https://rocsparse.readthedocs.io/en/master/'
license=('MIT')
depends=('hip')
makedepends=('cmake' 'git' 'gcc-fortran' 'python')
optdepends=('gcc-fortran: Use Fortran wrapper'
            'python: Use Python wrapper')
_git='https://github.com/ROCmSoftwarePlatform/rocRAND'
_hiprand='https://github.com/ROCmSoftwarePlatform/hipRAND'
source=("$pkgname-$pkgver.tar.gz::$_git/archive/rocm-$pkgver.tar.gz"
        "$pkgname-hiprand-$pkgver.tar.gz::$_hiprand/archive/20ac3db9d7462c15a3e96a6f0507cd5f2ee089c4.tar.gz")
sha256sums=('be4c9f9433415bdfea50d9f47b8afb43ac315f205ed39674f863955a6c256dca'
            'ee38a68c9e88056b7ecd41553e496e455dbb3fe08871ff3545430d6733070e6b')
_dirname="$(basename "$_git")-$(basename "${source[0]}" ".tar.gz")"
_hipname="$(basename "$_hiprand")-$(basename "${source[1]}" ".tar.gz")"

prepare() {
  rm -r "$srcdir/$_dirname/hipRAND"
  ln -s "$srcdir/$_hipname" "$srcdir/$_dirname/hipRAND"
}

build() {
  # -fcf-protection is not supported by HIP, see
  # https://docs.amd.com/bundle/ROCm-Compiler-Reference-Guide-v5.3/page/Appendix_A.html
  CXXFLAGS="${CXXFLAGS} -fcf-protection=none" \
  cmake \
    -Wno-dev \
    -B build \
    -S "$_dirname" \
    -DCMAKE_CXX_COMPILER=/opt/rocm/hip/bin/hipcc \
    -DCMAKE_INSTALL_PREFIX=/opt/rocm \
    -DBUILD_TEST=OFF
  cmake --build build
}

package() {
  DESTDIR="$pkgdir" cmake --install build

  echo '/opt/rocm/hiprand/lib' > rocrand.conf
  echo '/opt/rocm/rocrand/lib' >> rocrand.conf
  install -Dm644 rocrand.conf "$pkgdir/etc/ld.so.conf.d/$pkgname.conf"
  install -Dm644 "$_dirname/LICENSE.txt" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
