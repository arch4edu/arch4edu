# Maintainer: Gilbert Gilb's <gilbsgilbert@gmail.com>
pkgname=riscv64-gnu-toolchain-elf-bin
pkgver=2026.07.15
pkgrel=1
pkgdesc="GNU toolchain for riscv64 ELF, including GCC."
arch=('x86_64')
url="https://github.com/riscv-collab/riscv-gnu-toolchain"
license=('GPL2')
provides=(
)
conflicts=(
  'riscv64-gnu-toolchain-elf-llvm-bin'
)
optdepends=()
makedepends=()
options=(!strip)
source=(
  "riscv64-gnu-toolchain-elf-bin-2026.07.15-riscv64-elf-ubuntu-24.04-gcc.tar.xz::https://github.com/riscv-collab/riscv-gnu-toolchain/releases/download/2026.07.15/riscv64-elf-ubuntu-24.04-gcc.tar.xz"
)
sha512sums=(
  "b2945f1e3b6ca03716fec845ff7fb01b32558450c2b00d624b977477250deed5fd930d991451009ecd19d2eaeba1e40a2b2b76ae9e9928fdb5e8b777d5aa2262"
)

package() {
  install -dm755 "${pkgdir}"/opt/riscv64-gnu-toolchain-elf-bin "${pkgdir}"/usr/bin "${pkgdir}"/usr/lib/gcc
  cp -pR "${srcdir}"/riscv/* "${pkgdir}"/opt/riscv64-gnu-toolchain-elf-bin

  # Install sysroot
  if test -d "${pkgdir}"/opt/riscv64-gnu-toolchain-elf-bin/sysroot; then
    sysroot=/opt/riscv64-gnu-toolchain-elf-bin/sysroot
  else
    sysroot=/opt/riscv64-gnu-toolchain-elf-bin/riscv64-unknown-elf
  fi
  ln -s "${sysroot}" "${pkgdir}"/usr/riscv64-unknown-elf

  # Install cross libgcc
  ln -s /opt/riscv64-gnu-toolchain-elf-bin/lib/gcc/riscv64-unknown-elf "${pkgdir}"/usr/lib/gcc

  # Install binaries
  for f in "${srcdir}"/riscv/bin/riscv64-unknown-elf-*; do
    f="$(basename "${f}")"
    ln -s /opt/riscv64-gnu-toolchain-elf-bin/bin/"${f}" "${pkgdir}"/usr/bin
  done

  # Also provide target quadruplet to prevent confusing clang
  ln -s riscv64-unknown-elf "${pkgdir}"/usr/riscv64-unknown-unknown-elf
  ln -s riscv64-unknown-elf "${pkgdir}"/usr/lib/gcc/riscv64-unknown-unknown-elf
  find \
    "${pkgdir}" \
    -name riscv64-unknown-elf \
    -type d \
    -exec /bin/sh -c 'ln -s riscv64-unknown-elf "$(dirname "$0")"/riscv64-unknown-unknown-elf' {} \;

  # Strip
  find \
    "${pkgdir}"/opt/riscv64-gnu-toolchain-elf-bin/bin \
    "${pkgdir}"/opt/riscv64-gnu-toolchain-elf-bin/lib \
    "${pkgdir}"/opt/riscv64-gnu-toolchain-elf-bin/libexec \
    -type f \
    -exec /bin/sh -c 'if file --no-sandbox "$0" | grep -qE "ELF.*(executable|shared object)"; then strip "$0"; fi' {} \;
}