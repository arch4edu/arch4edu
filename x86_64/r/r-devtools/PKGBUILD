# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Kibouo <csonka.mihaly@hotmail.com>
# Contributor: Ward Segers <w@rdsegers.be>
# Contributor: Alex Branham <branham@utexas.edu>

_pkgname=devtools
_pkgver=2.5.2
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//[:-]/.}
pkgrel=1
pkgdesc='Tools to Make Developing R Packages Easier'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('MIT')
depends=(
  r-cli
  r-desc
  r-ellipsis
  r-fs
  r-lifecycle
  r-memoise
  r-miniui
  r-pak
  r-pkgbuild
  r-pkgdown
  r-pkgload
  r-profvis
  r-rcmdcheck
  r-rlang
  r-roxygen2
  r-rversions
  r-sessioninfo
  r-testthat
  r-urlchecker
  r-withr
  r-usethis
)
optdepends=(
  r-biocmanager
  r-callr
  r-covr
  r-curl
  r-digest
  r-dt
  r-foghorn
  r-gh
  r-knitr
  r-lintr
  r-rmarkdown
  r-rstudioapi
  r-spelling
  r-httr2
  r-quarto
  r-remotes
  r-xml2
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('ea50645bc1402d6c746aff77f0c22c8e')
b2sums=('5cf74751c4a6852c4f6b01fe3ca72bd1e6d5152ad2a14170f5eaa06caddc6ba147c801a2df2df704a422d92937a1e89f0dc143ad092f5eb85ae1a37d1433a205')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
  install -Dm644 "${_pkgname}/LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
