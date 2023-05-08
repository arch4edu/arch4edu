# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=metafor
_pkgver=4.2-0
pkgname=r-${_pkgname,,}
pkgver=4.2.0
pkgrel=1
pkgdesc='Meta-Analysis Package for R'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
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
  r-rvmmin
  r-sp
  r-subplex
  r-survival
  r-testthat
  r-ucminf
  r-wildmeta
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('f1bb423b4f568c1af9b2c21bf368308b054bcb83d39a9d67273e43596be0a766')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
