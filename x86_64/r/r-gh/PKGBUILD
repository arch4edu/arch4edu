# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=gh
_pkgver=1.5.0
pkgname=r-${_pkgname,,}
pkgver=1.5.0
pkgrel=1
pkgdesc="'GitHub' 'API'"
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('MIT')
depends=(
  r
  r-cli
  r-gitcreds
  r-httr2
  r-ini
  r-jsonlite
  r-rlang
)
optdepends=(
  r-covr
  r-knitr
  r-mockery
  r-rmarkdown
  r-rprojroot
  r-spelling
  r-testthat
  r-withr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('295a063084960fc790156d75e1db8b653d6123441079b2c94f1a8937e0329b8e')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
  install -Dm644 "${_pkgname}/LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
