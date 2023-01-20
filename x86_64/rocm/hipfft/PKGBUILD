# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>

pkgname=hipfft
pkgver=5.4.1
pkgrel=1
pkgdesc='rocFFT marshalling library.'
arch=('x86_64')
url='https://hipfft.readthedocs.io/en/latest/'
license=('MIT')
depends=('hip' 'rocfft')
makedepends=('rocm-cmake')
_git='https://github.com/ROCmSoftwarePlatform/hipFFT'
source=("$pkgname-$pkgver.tar.gz::$_git/archive/rocm-$pkgver.tar.gz"
        "hipfft-no-git.patch")
sha256sums=('6ebe66858418f71ae13b14ef36628e3c6b6cd116964372c95ff241ed3082dce4'
            '6bf435844134dc8e8909ec3f1b73e210e82d61b00b8a555106bd1570fda3294a')
_dirname="$(basename "$_git")-$(basename "${source[0]}" ".tar.gz")"

prepare() {
    cd "$_dirname"
    patch -Np1 -i "$srcdir/hipfft-no-git.patch"
}

build() {
  # -fcf-protection is not supported by HIP, see
  # https://docs.amd.com/bundle/ROCm-Compiler-Reference-Guide-v5.4/page/Appendix_A.html
  CXXFLAGS="${CXXFLAGS} -fcf-protection=none" \
  ROCM_PATH=/opt/rocm \
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

  echo "/opt/rocm/$pkgname/lib" > "$pkgname.conf"
  install -Dm644 "$pkgname.conf" "$pkgdir/etc/ld.so.conf.d/hipfft.conf"

  install -Dm644 "$srcdir/$_dirname/LICENSE.md" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
