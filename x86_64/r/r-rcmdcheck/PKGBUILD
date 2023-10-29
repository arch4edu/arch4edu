# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=rcmdcheck
_pkgver=1.4.0
pkgname=r-${_pkgname,,}
pkgver=1.4.0
pkgrel=7
pkgdesc="Run 'R CMD check' from 'R' and Capture Results"
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('MIT')
depends=(
  r
  r-callr
  r-cli
  r-curl
  r-desc
  r-digest
  r-pkgbuild
  r-prettyunits
  r-r6
  r-rprojroot
  r-sessioninfo
  r-withr
  r-xopen
)
optdepends=(
  r-covr
  r-knitr
  r-mockery
  r-processx
  r-ps
  r-rmarkdown
  r-svglite
  r-testthat
  r-webfakes
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('bbd4ef7d514b8c2076196a7c4a6041d34623d55fbe73f2771758ce61fd32c9d0')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
  install -Dm644 "${_pkgname}/LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
