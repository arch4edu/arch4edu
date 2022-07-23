# Maintainer Torsten Keßler <t dot kessler at posteo dot de>

pkgname=hipsolver
pkgver=5.2.0
pkgrel=1
pkgdesc='rocSOLVER marshalling library.'
arch=('x86_64')
url='https://hipsolver.readthedocs.io/en/latest/index.html'
license=('MIT')
depends=('hip' 'rocsolver')
makedepends=('cmake' 'git' 'gcc-fortran')
_git='https://github.com/ROCmSoftwarePlatform/hipSOLVER'
source=("$pkgname-$pkgver.tar.gz::$_git/archive/rocm-$pkgver.tar.gz")
sha256sums=('96927410e0a2cc0f50172604ef6437e15d2cf4b62d22b2035f13aae21f43dc82')
_dirname="$(basename "$_git")-$(basename "${source[0]}" ".tar.gz")"

build() {
  # -fcf-protection is not supported by HIP, see
  # https://docs.amd.com/bundle/ROCm-Compiler-Reference-Guide-v5.2/page/Appendix_A.html
  CXX=/opt/rocm/bin/hipcc \
  CXXFLAGS="${CXXFLAGS} -fcf-protection=none" \
  cmake -Wno-dev -S "$_dirname" \
        -DCMAKE_INSTALL_PREFIX=/opt/rocm
  make
}

package() {
  DESTDIR="$pkgdir" make install

  install -Dm644 /dev/stdin "$pkgdir/etc/ld.so.conf.d/hipsolver.conf" << EOF
/opt/rocm/hipsolver/lib
EOF
  install -Dm644 "$srcdir/$_dirname/LICENSE.md" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
