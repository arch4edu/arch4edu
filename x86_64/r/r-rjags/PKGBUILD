# system requirements: JAGS 4.x.y
# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=rjags
_pkgver=4-15
pkgname=r-${_pkgname,,}
pkgver=4.15
pkgrel=1
pkgdesc='Bayesian Graphical Models using MCMC'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-coda
  jags
)
optdepends=(
  r-tcltk
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('35cd4c1faaaa8523b87ac053b881dccf29798f073f438459589e786b95ef18a1')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
