# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=BDgraph
_pkgver=2.72
pkgname=r-${_pkgname,,}
pkgver=2.72
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
sha256sums=('7cf9cc1bccf2a56b518c88030e00e88217f571afcb250aa95c3bd2771a8b83cd')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
