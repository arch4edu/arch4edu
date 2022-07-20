# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=metafor
_pkgver=3.4-0
pkgname=r-${_pkgname,,}
pkgver=3.4.0
pkgrel=1
pkgdesc='Meta-Analysis Package for R'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-mathjaxr
  r-pbapply
  r-metadat
)
optdepends=(
  r-ape
  r-biasedurn
  r-boot
  r-compquadform
  r-crayon
  r-dfoptim
  r-epi
  r-glmmadaptive
  r-gsl
  r-lme4
  r-minqa
  r-multcomp
  r-mvtnorm
  r-nloptr
  r-numderiv
  r-optimparallel
  r-r.rsp
  r-rmarkdown
  r-sp
  r-survival
  r-testthat
  r-ucminf
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('92e1bc21c4d135b6e651fbefc4b40666fc02c66a6a4f6f28effee0e73a21c26e')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
