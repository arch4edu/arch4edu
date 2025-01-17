# Maintainer: Gilbert Gilb's <gilbsgilbert@gmail.com>
pkgname=riscv64-gnu-toolchain-glibc-bin
pkgver=2025.01.16
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
  "https://github.com/riscv-collab/riscv-gnu-toolchain/releases/download/2025.01.16/riscv64-glibc-ubuntu-24.04-gcc-nightly-2025.01.16-nightly.tar.xz"
)
sha512sums=(
  "fb50c64b1649dfa4d05351f8d42ab1787c3a656708085aeb69624d27401f5f58b654d09536c5914ed84c26b96c68128047d07e1832908fff94253a35ccadb9bb"
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