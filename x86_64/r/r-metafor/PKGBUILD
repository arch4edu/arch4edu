# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=metafor
_pkgver=4.8-0
pkgname=r-${_pkgname,,}
pkgver=4.8.0
pkgrel=2
pkgdesc='Meta-Analysis Package for R'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-digest
  r-mathjaxr
  r-metadat
  r-numderiv
  r-pbapply
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
  r-emmeans
  r-epi
  r-estmeansd
  r-glmmadaptive
  r-glmmtmb
  r-gsl
  r-lbfgsb3c
  r-lme4
  r-metablue
  r-minqa
  r-multcomp
  r-mvtnorm
  r-nloptr
  r-optimparallel
  r-pracma
  r-r.rsp
  r-rcgmin
  r-rmarkdown
  r-rsolnp
  r-rstudioapi
  r-rvmmin
  r-sp
  r-subplex
  r-survival
  r-testthat
  r-ucminf
  r-wildmeta
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('2b710674b15fe3e79474b5c3e779038a614eba9e61b2249532c86dc155f00644')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
