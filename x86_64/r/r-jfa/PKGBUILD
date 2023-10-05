# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=jfa
_pkgver=0.7.0
pkgname=r-${_pkgname,,}
pkgver=0.7.0
pkgrel=1
pkgdesc='Bayesian and Classical Audit Sampling'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-bde
  r-bh
  r-extradistr
  r-ggplot2
  r-rcpp
  r-rcppeigen
  r-rcppparallel
  r-rstan
  r-rstantools
  r-stanheaders
  r-truncdist
)
optdepends=(
  r-benford.analysis
  r-benfordtests
  r-beyondbenford
  r-kableextra
  r-knitr
  r-mus
  r-rmarkdown
  r-samplingbook
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('a748c6521121c989a87af0631871903c7418b9cb9f5da87646fee61bc479d794')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
