# Maintainer: Eric Berquist <eric DOT berquist AT gmail DOT com>

_name=cp2k
pkgname=${_name}-bin
pkgver=2026.2
pkgrel=1
pkgdesc="A quantum chemistry and solid state physics software package for atomistic simulations of solid state, liquid, molecular, periodic, material, crystal, and biological systems. (precompiled, OpenMP)"
arch=("x86_64")
url="https://www.cp2k.org"
license=("GPL2")
provides=("${_name}")
conflicts=("${_name}")
source_x86_64=("https://github.com/${_name}/${_name}/releases/download/v${pkgver}/${_name}-${pkgver}-Linux-gnu-x86_64.ssmp")
# No aarch64 binary available for 2026.1
sha256sums_x86_64=('1497870e84fc4092890d1345a7ea8f61922cc162ced32cab86e359a7b9142b6f')

package() {
  cd "${srcdir}"

  install -Dm755 "${_name}-${pkgver}-Linux-gnu-${CARCH}.ssmp" "${pkgdir}"/usr/bin/"${_name}"
}
