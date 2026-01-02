# Maintainer: Gilbert Gilb's <gilbsgilbert@gmail.com>
pkgname=riscv64-gnu-toolchain-elf-bin
pkgver=2026.01.01
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
  "riscv64-gnu-toolchain-elf-bin-2026.01.01-riscv64-elf-ubuntu-24.04-gcc.tar.xz::https://github.com/riscv-collab/riscv-gnu-toolchain/releases/download/2026.01.01/riscv64-elf-ubuntu-24.04-gcc.tar.xz"
)
sha512sums=(
  "bc98296771447a8d554bd3411a56a88c8e39e0043bf04ddc7927b400526bab947e3bc47c4d7fb79fc68c55d3ac5802101c2cb362ff77be7e88dcf92cbd10bd03"
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