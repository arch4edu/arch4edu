# Maintainer Torsten Keßler <t dot kessler at posteo dot de>

pkgname=rocsolver
pkgver=4.0.0
pkgrel=1
pkgdesc='Subset of LAPACK functionality on the ROCm platform'
arch=('x86_64')
url='https://rocsolver.readthedocs.io/en/latest/userguidedocu.html'
license=('BSD 2-Clause')
depends=('hip-rocclr' 'rocblas')
makedepends=('cmake' 'python' 'python-pyaml' 'rocm-cmake')
_git='https://github.com/ROCmSoftwarePlatform/rocSOLVER'
source=("$pkgname-$pkgver.tar.gz::$_git/archive/rocm-$pkgver.tar.gz")
sha256sums=('be9a52644c276813f76d78f2c11eddaf8c2d7f9dd04f4570f23d328ad30d5880')
_dirname="$(basename "$_git")-$(basename "${source[0]}" .tar.gz)"

build() {
    CXX=/opt/rocm/hip/bin/hipcc \
    cmake   -B build -Wno-dev \
            -S "$_dirname" \
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
