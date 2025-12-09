# Maintainer: Gilbert Gilb's <gilbsgilbert@gmail.com>
pkgname=riscv32-gnu-toolchain-glibc-bin
pkgver=2025.11.27
pkgrel=1
pkgdesc="GNU toolchain for riscv32 Linux, including GCC."
arch=('x86_64')
url="https://github.com/riscv-collab/riscv-gnu-toolchain"
license=('GPL2')
provides=(
)
conflicts=(
  'riscv32-gnu-toolchain-glibc-llvm-bin'
)
optdepends=()
makedepends=()
options=(!strip)
source=(
  "https://github.com/riscv-collab/riscv-gnu-toolchain/releases/download/2025.11.27/riscv32-glibc-ubuntu-24.04-gcc.tar.xz"
)
sha512sums=(
  "aed044c1f9d7be5d797c8b10fd2a3d1131c202f8023d6c294fa1bc9b696b175cf86f91aad6126c9e51dd3f94566ba360e75bbfb2c6ee9c911f1a42164a40c5eb"
)

package() {
  install -dm755 "${pkgdir}"/opt/riscv32-gnu-toolchain-glibc-bin "${pkgdir}"/usr/bin "${pkgdir}"/usr/lib/gcc
  cp -pR "${srcdir}"/riscv/* "${pkgdir}"/opt/riscv32-gnu-toolchain-glibc-bin

  # Install sysroot
  if test -d "${pkgdir}"/opt/riscv32-gnu-toolchain-glibc-bin/sysroot; then
    sysroot=/opt/riscv32-gnu-toolchain-glibc-bin/sysroot
  else
    sysroot=/opt/riscv32-gnu-toolchain-glibc-bin/riscv32-unknown-linux-gnu
  fi
  ln -s "${sysroot}" "${pkgdir}"/usr/riscv32-unknown-linux-gnu

  # Install cross libgcc
  ln -s /opt/riscv32-gnu-toolchain-glibc-bin/lib/gcc/riscv32-unknown-linux-gnu "${pkgdir}"/usr/lib/gcc

  # Install binaries
  for f in "${srcdir}"/riscv/bin/riscv32-unknown-linux-gnu-*; do
    f="$(basename "${f}")"
    ln -s /opt/riscv32-gnu-toolchain-glibc-bin/bin/"${f}" "${pkgdir}"/usr/bin
  done

  

  # Strip
  find \
    "${pkgdir}"/opt/riscv32-gnu-toolchain-glibc-bin/bin \
    "${pkgdir}"/opt/riscv32-gnu-toolchain-glibc-bin/lib \
    "${pkgdir}"/opt/riscv32-gnu-toolchain-glibc-bin/libexec \
    -type f \
    -exec /bin/sh -c 'if file --no-sandbox "$0" | grep -qE "ELF.*(executable|shared object)"; then strip "$0"; fi' {} \;
}