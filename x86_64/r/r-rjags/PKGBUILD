# system requirements: JAGS 4.x.y
# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=rjags
_pkgver=4-13
pkgname=r-${_pkgname,,}
pkgver=4.13
pkgrel=5
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
sha256sums=('f85cc34c5127b828d8a3fa3613ef29f147c868bdaf55eb0f7406c10abbf92b32')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
