# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=metamisc
_pkgver=0.4.0
pkgname=r-${_pkgname,,}
pkgver=0.4.0
pkgrel=1
pkgdesc='Meta-Analysis of Diagnosis and Prognosis Research Studies'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-dplyr
  r-ggplot2
  r-lme4
  r-metafor
  r-mvtnorm
  r-plyr
  r-proc
)
optdepends=(
  r-coda
  r-ggmcmc
  r-logistf
  r-rjags
  r-runjags
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('4a43832dcc232acd1da963d0113396af42c388d7763a8a3ad8479d68efdccd8b')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
