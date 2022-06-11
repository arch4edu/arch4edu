# Maintainer Torsten Keßler <t dot kessler at posteo dot de>

pkgname=rocsolver
pkgver=4.3.1
pkgrel=1
pkgdesc='Subset of LAPACK functionality on the ROCm platform'
arch=('x86_64')
url='https://rocsolver.readthedocs.io/en/latest/userguidedocu.html'
license=('BSD 2-Clause')
depends=('hip-rocclr' 'rocblas')
makedepends=('cmake' 'python' 'python-pyaml' 'rocm-cmake')
_git='https://github.com/ROCmSoftwarePlatform/rocSOLVER'
source=("$pkgname-$pkgver.tar.gz::$_git/archive/rocm-$pkgver.tar.gz")
sha256sums=('c6e7468d7041718ce6e1c7f50ec80a552439ac9cfed2dc3f753ae417dda5724f')
_dirname="$(basename "$_git")-$(basename "${source[0]}" .tar.gz)"

build() {
    # -fcf-protection is not supported by HIP, see
    # https://github.com/ROCm-Developer-Tools/HIP/blob/rocm-4.3.x/docs/markdown/clang_options.md
    
    # With version 3.21, HIP support was added to CMake that breaks the current scripts, see
    # https://github.com/ROCmSoftwarePlatform/rocRAND/issues/198#issuecomment-893573440
    CXX=/opt/rocm/bin/hipcc \
    CXXFLAGS="${CXXFLAGS} -fcf-protection=none" \
    cmake   -B build -Wno-dev \
            -S "$_dirname" \
            -D__skip_rocmclang=ON \
            -DCMAKE_INSTALL_PREFIX=/opt/rocm \
            -DCMAKE_PREFIX_PATH=/opt/rocm/llvm/lib/cmake/llvm \
            -DBUILD_CLIENTS_TESTS=OFF \
            -DBUILD_CLIENTS_BENCHMARKS=OFF
    make -C build
}

package() {
    DESTDIR="$pkgdir" make -C build install

    install -Dm644 /dev/stdin "$pkgdir/etc/ld.so.conf.d/$pkgname.conf" <<-EOF
        /opt/rocm/$pkgname/lib
EOF
    install -Dm644 "$_dirname/LICENSE.md" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
