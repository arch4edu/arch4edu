# Maintainer: Gilbert Gilb's <gilbsgilbert@gmail.com>
pkgname=riscv32-gnu-toolchain-elf-bin
pkgver=2025.11.27
pkgrel=2
pkgdesc="GNU toolchain for riscv32 ELF, including GCC."
arch=('x86_64')
url="https://github.com/riscv-collab/riscv-gnu-toolchain"
license=('GPL2')
provides=(
)
conflicts=(
  'riscv32-gnu-toolchain-elf-llvm-bin'
)
optdepends=()
makedepends=()
options=(!strip)
source=(
  "riscv32-gnu-toolchain-elf-bin-2025.11.27-riscv32-elf-ubuntu-24.04-gcc.tar.xz::https://github.com/riscv-collab/riscv-gnu-toolchain/releases/download/2025.11.27/riscv32-elf-ubuntu-24.04-gcc.tar.xz"
)
sha512sums=(
  "a570f5f526ed700dc16360b8790ed9dcced1d7eafbf365a5d5fb53522d59899fa66ad4897fa72de1fbf881f3235b7e9c0f1a9dec7f61f0f6d45bbc5ad038b86e"
)

package() {
  install -dm755 "${pkgdir}"/opt/riscv32-gnu-toolchain-elf-bin "${pkgdir}"/usr/bin "${pkgdir}"/usr/lib/gcc
  cp -pR "${srcdir}"/riscv/* "${pkgdir}"/opt/riscv32-gnu-toolchain-elf-bin

  # Install sysroot
  if test -d "${pkgdir}"/opt/riscv32-gnu-toolchain-elf-bin/sysroot; then
    sysroot=/opt/riscv32-gnu-toolchain-elf-bin/sysroot
  else
    sysroot=/opt/riscv32-gnu-toolchain-elf-bin/riscv32-unknown-elf
  fi
  ln -s "${sysroot}" "${pkgdir}"/usr/riscv32-unknown-elf

  # Install cross libgcc
  ln -s /opt/riscv32-gnu-toolchain-elf-bin/lib/gcc/riscv32-unknown-elf "${pkgdir}"/usr/lib/gcc

  # Install binaries
  for f in "${srcdir}"/riscv/bin/riscv32-unknown-elf-*; do
    f="$(basename "${f}")"
    ln -s /opt/riscv32-gnu-toolchain-elf-bin/bin/"${f}" "${pkgdir}"/usr/bin
  done

  # Also provide target quadruplet to prevent confusing clang
  ln -s riscv32-unknown-elf "${pkgdir}"/usr/riscv32-unknown-unknown-elf
  ln -s riscv32-unknown-elf "${pkgdir}"/usr/lib/gcc/riscv32-unknown-unknown-elf
  find \
    "${pkgdir}" \
    -name riscv32-unknown-elf \
    -type d \
    -exec /bin/sh -c 'ln -s riscv32-unknown-elf "$(dirname "$0")"/riscv32-unknown-unknown-elf' {} \;

  # Strip
  find \
    "${pkgdir}"/opt/riscv32-gnu-toolchain-elf-bin/bin \
    "${pkgdir}"/opt/riscv32-gnu-toolchain-elf-bin/lib \
    "${pkgdir}"/opt/riscv32-gnu-toolchain-elf-bin/libexec \
    -type f \
    -exec /bin/sh -c 'if file --no-sandbox "$0" | grep -qE "ELF.*(executable|shared object)"; then strip "$0"; fi' {} \;
}