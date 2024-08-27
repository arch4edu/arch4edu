# Maintainer: Eric Berquist <eric DOT berquist AT gmail DOT com>

_name=cp2k
pkgname=${_name}-bin
pkgver=2024.2
pkgrel=1
pkgdesc="A quantum chemistry and solid state physics software package for atomistic simulations of solid state, liquid, molecular, periodic, material, crystal, and biological systems. (precompiled, OpenMP)"
arch=("x86_64" "aarch64")
url="https://www.cp2k.org"
license=("GPL2")
provides=("${_name}")
conflicts=("${_name}")
source_x86_64=("https://github.com/${_name}/${_name}/releases/download/v${pkgver}/${_name}-${pkgver}-Linux-gnu-x86_64.ssmp")
source_aarch64=("https://github.com/${_name}/${_name}/releases/download/v${pkgver}/${_name}-${pkgver}-Linux-gnu-aarch64.ssmp")
md5sums_x86_64=('cb0641976ec21809b48a7f48aa4bd331')
md5sums_aarch64=('efc96727e78144a926a3e5d2424bc124')

package() {
  cd "${srcdir}"

  install -Dm755 "${_name}-${pkgver}-Linux-gnu-${CARCH}.ssmp" "${pkgdir}"/usr/bin/"${_name}"
}
