# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=BDgraph
_pkgver=2.73
pkgname=r-${_pkgname,,}
pkgver=2.73
pkgrel=1
pkgdesc='Bayesian Structure Learning in Graphical Models using Birth-Death MCMC'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-ggplot2
  r-igraph
  r-proc
)
optdepends=(
  r-huge
  r-knitr
  r-rmarkdown
  r-skimr
  r-ssgraph
  r-tmvtnorm
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('90aa89b7f717c10105cf612b5cb7bf40d0c94732cb3bb26e02d42496cbf0c12d')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
