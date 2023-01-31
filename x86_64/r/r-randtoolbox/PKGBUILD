# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=randtoolbox
_pkgver=2.0.4
pkgname=r-${_pkgname,,}
pkgver=2.0.4
pkgrel=1
pkgdesc='Toolbox for Pseudo and Quasi Random Number Generation and Random Generator Tests'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('BSD')
depends=(
  r
  r-rngwell
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('94da14953e4ffc7981d7a9398622082c4eda3bd9d912d1437b527d949da39e4b')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
  install -Dm644 "${_pkgname}/LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
