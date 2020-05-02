# Submitter: Olaf Leidinger <oleid@mescharet.de>
# Maintainer: Jakub Okoński <jakub@okonski.org>
# Maintainer: Rigo Reddig <rigo.reddig@gmail.com> ;)
# Maintainer: Markus Näther <naetherm@cs.uni-freiburg.de>
pkgname=hcc
pkgver=3.3.0
pkgrel=3
pkgdesc='C++ Compiler for Heterogeneous Compute'
arch=('x86_64')
url="https://github.com/RadeonOpenCompute/hcc"
license=('custom:NCSAOSL')
depends=("hsa-rocr>=$pkgver" 'z3')
makedepends=('cmake' 'python')
options=(!staticlibs strip)
source=("hcc-roc-hcc-$pkgver.tar.gz::https://github.com/RadeonOpenCompute/hcc/archive/roc-hcc-$pkgver.tar.gz"
        "llvm-project-roc-hcc-$pkgver.tar.gz::https://github.com/RadeonOpenCompute/llvm-project/archive/roc-hcc-$pkgver.tar.gz"
        "ROCm-Device-Libs-roc-hcc-$pkgver.tar.gz::https://github.com/RadeonOpenCompute/ROCm-Device-Libs/archive/roc-hcc-$pkgver.tar.gz")
sha256sums=('b134cbc9ccfdda0255edad95d06c11fac63bcdbffc1e4d14eb946833cedc9600'
            '37baed7d0130b38840ec00973d68d089f21798c27be91d0b9177b2e943945c0f'
            '7a82aac4390c468a8ba7060b7ba0ecef0c89856df4e2133ad74418264ae62aaf')

prepare() {
  cd "$srcdir"
  mv -T "llvm-project-roc-hcc-$pkgver" "hcc-roc-hcc-$pkgver/llvm-project"
  mv -T "ROCm-Device-Libs-roc-hcc-$pkgver" "hcc-roc-hcc-$pkgver/rocdl"

  cd "$srcdir/hcc-roc-hcc-$pkgver/llvm-project"
  #patch -Np1 -i "$srcdir/Fix-sanitizer-common-build-with-glibc-2.31.patch"
}

build() {
  mkdir -p "$srcdir/build"
  cd "$srcdir/build"

  cmake -DCMAKE_INSTALL_PREFIX=/opt/rocm/hcc \
        -DLLVM_INSTALL_UTILS=TRUE \
        "$srcdir/hcc-roc-hcc-$pkgver"

  make
}

package() {
  cd "$srcdir/build"

  make DESTDIR="$pkgdir" install

  # add links (extractkernel is for rocblas with tensile)
  install -d "$pkgdir/usr/bin"
  local _fn
  for _fn in hcc hcc-config extractkernel; do
    ln -s "/opt/rocm/hcc/bin/$_fn" "$pkgdir/usr/bin/$_fn"
  done

  # additional link to make hcc demos happy
  install -d "$pkgdir/opt/rocm/include"
  ln -s /opt/rocm/hcc/include "$pkgdir/opt/rocm/include/hcc"

  # additional link to make clang-ocl work
  ln -s /opt/rocm/hcc/bin "$pkgdir/opt/rocm/hcc/bin/x86_64"
}
