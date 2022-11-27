# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=metafor
_pkgver=3.8-1
pkgname=r-${_pkgname,,}
pkgver=3.8.1
pkgrel=3
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
  r-alabama
  r-ape
  r-bb
  r-biasedurn
  r-boot
  r-clubsandwich
  r-compquadform
  r-crayon
  r-dfoptim
  r-epi
  r-glmmadaptive
  r-glmmtmb
  r-gsl
  r-lbfgsb3c
  r-lme4
  r-minqa
  r-multcomp
  r-mvtnorm
  r-nloptr
  r-numderiv
  r-optimparallel
  r-pracma
  r-r.rsp
  r-rmarkdown
  r-rsolnp
  r-sp
  r-subplex
  r-survival
  r-testthat
  r-ucminf
  r-wildmeta
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('d694577f954144d8a5eeab6521fe1c87e68ddf9ecfd7ccc915d01533371b0514')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
