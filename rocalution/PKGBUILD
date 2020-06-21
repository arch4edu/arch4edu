# Maintainer: Markus Näther <naetherm@informatik.uni-freiburg.de>
pkgname=rocalution
pkgver=3.5.0
pkgrel=1
pkgdesc='Next generation library for iterative sparse solvers for ROCm platform'
arch=('x86_64')
url='https://rocalution.readthedocs.io/en/master'
license=('MIT')
depends=('hip-rocclr' 'rocsparse' 'rocblas' 'rocprim' 'rocminfo' 'openmp')
makedepends=('cmake' 'git')
_git='https://github.com/ROCmSoftwarePlatform/rocALUTION'
source=("$pkgname-$pkgver.tar.gz::$_git/archive/rocm-$pkgver.tar.gz")
sha256sums=('be2f78c10c100d7fd9df5dd2403a44700219c2cbabaacf2ea50a6e2241df7bfe')

build() {
  CXX=/opt/rocm/hip/bin/hipcc \
  cmake -B build -Wno-dev \
        -DCMAKE_INSTALL_PREFIX=/opt/rocm \
        -DSUPPORT_HIP=ON \
        -DSUPPORT_OMP=ON \
        -DSUPPORT_MPI=OFF \
        -Dhip_DIR=/opt/rocm/hip/lib/cmake/hip \
        -Damd_comgr_DIR=/opt/rocm/lib/cmake/amd_comgr \
        "$srcdir/rocALUTION-rocm-$pkgver"
  make -C build
}

package() {
  DESTDIR="$pkgdir" make -C build install

  install -Dm644 /dev/stdin "$pkgdir/etc/ld.so.conf.d/rocalution.conf" << EOF
/opt/rocm/rocalution/lib
EOF
  install -Dm644 "$srcdir/rocALUTION-rocm-$pkgver/LICENSE.md" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
