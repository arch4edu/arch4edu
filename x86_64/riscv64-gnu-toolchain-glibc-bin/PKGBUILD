# Maintainer: Gilbert Gilb's <gilbsgilbert@gmail.com>
pkgname=riscv64-gnu-toolchain-glibc-bin
pkgver=2025.12.30
pkgrel=1
pkgdesc="GNU toolchain for riscv64 Linux, including GCC."
arch=('x86_64')
url="https://github.com/riscv-collab/riscv-gnu-toolchain"
license=('GPL2')
provides=(
)
conflicts=(
  'riscv64-gnu-toolchain-glibc-llvm-bin'
)
optdepends=()
makedepends=()
options=(!strip)
source=(
  "riscv64-gnu-toolchain-glibc-bin-2025.12.30-riscv64-glibc-ubuntu-24.04-gcc.tar.xz::https://github.com/riscv-collab/riscv-gnu-toolchain/releases/download/2025.12.30/riscv64-glibc-ubuntu-24.04-gcc.tar.xz"
)
sha512sums=(
  "49977b235072220363ff73577101364395c38c57edaede2c0070cfdd583a63005d7154636c9b0bdc9a2e700532c1397d4935de6ac2ed24b3cb028258608a7cd8"
)

package() {
  install -dm755 "${pkgdir}"/opt/riscv64-gnu-toolchain-glibc-bin "${pkgdir}"/usr/bin "${pkgdir}"/usr/lib/gcc
  cp -pR "${srcdir}"/riscv/* "${pkgdir}"/opt/riscv64-gnu-toolchain-glibc-bin

  # Install sysroot
  if test -d "${pkgdir}"/opt/riscv64-gnu-toolchain-glibc-bin/sysroot; then
    sysroot=/opt/riscv64-gnu-toolchain-glibc-bin/sysroot
  else
    sysroot=/opt/riscv64-gnu-toolchain-glibc-bin/riscv64-unknown-linux-gnu
  fi
  ln -s "${sysroot}" "${pkgdir}"/usr/riscv64-unknown-linux-gnu

  # Install cross libgcc
  ln -s /opt/riscv64-gnu-toolchain-glibc-bin/lib/gcc/riscv64-unknown-linux-gnu "${pkgdir}"/usr/lib/gcc

  # Install binaries
  for f in "${srcdir}"/riscv/bin/riscv64-unknown-linux-gnu-*; do
    f="$(basename "${f}")"
    ln -s /opt/riscv64-gnu-toolchain-glibc-bin/bin/"${f}" "${pkgdir}"/usr/bin
  done

  

  # Strip
  find \
    "${pkgdir}"/opt/riscv64-gnu-toolchain-glibc-bin/bin \
    "${pkgdir}"/opt/riscv64-gnu-toolchain-glibc-bin/lib \
    "${pkgdir}"/opt/riscv64-gnu-toolchain-glibc-bin/libexec \
    -type f \
    -exec /bin/sh -c 'if file --no-sandbox "$0" | grep -qE "ELF.*(executable|shared object)"; then strip "$0"; fi' {} \;
}