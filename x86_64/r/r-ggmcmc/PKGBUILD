# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=ggmcmc
_pkgver=1.5.1.2
pkgname=r-${_pkgname,,}
pkgver=1.5.1.2
pkgrel=1
pkgdesc='Tools for Analyzing MCMC Simulations from Bayesian Inference'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-dplyr
  r-ggally
  r-ggplot2
  r-tidyr
)
optdepends=(
  r-cairo
  r-coda
  r-extrafont
  r-ggthemes
  r-gridextra
  r-knitr
  r-rmarkdown
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('a47bf2233d53017c59693ae0bd6c42d2f280c14d88746b350048400fa177b55e')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
