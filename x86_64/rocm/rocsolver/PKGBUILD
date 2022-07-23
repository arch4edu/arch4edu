# Maintainer Torsten Keßler <t dot kessler at posteo dot de>

pkgname=rocsolver
pkgver=5.2.0
pkgrel=1
pkgdesc='Subset of LAPACK functionality on the ROCm platform'
arch=('x86_64')
url='https://rocsolver.readthedocs.io/en/latest/'
license=('BSD 2-Clause')
depends=('hip' 'rocblas' 'fmt')
makedepends=('cmake' 'python' 'python-pyaml' 'rocm-cmake')
_git='https://github.com/ROCmSoftwarePlatform/rocSOLVER'
source=("$pkgname-$pkgver.tar.gz::$_git/archive/rocm-$pkgver.tar.gz")
sha256sums=('94d46ebe1266eaa05df50c1789dc27d3f2dbf3cb5af156e757777a82ed6ef356')
options=(!lto)
_dirname="$(basename "$_git")-$(basename "${source[0]}" .tar.gz)"

build() {
    local cmake_args=(-DCMAKE_INSTALL_PREFIX=/opt/rocm)
    if [[ -n "$AMDGPU_TARGETS" ]]; then
        cmake_args+=(-DAMDGPU_TARGETS="$AMDGPU_TARGETS")
    fi
    # -fcf-protection is not supported by HIP, see
    # https://docs.amd.com/bundle/ROCm-Compiler-Reference-Guide-v5.2/page/Appendix_A.html
    CXX=/opt/rocm/bin/hipcc \
    CXXFLAGS="${CXXFLAGS} -fcf-protection=none" \
    cmake   -B build \
            -S "$_dirname" \
            "${cmake_args[@]}"
    make -C build
}

package() {
    DESTDIR="$pkgdir" make -C build install

    install -Dm644 /dev/stdin "$pkgdir/etc/ld.so.conf.d/$pkgname.conf" <<-EOF
        /opt/rocm/$pkgname/lib
EOF
    install -Dm644 "$_dirname/LICENSE.md" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
