# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=mclust
_pkgver=6.0.0
pkgname=r-${_pkgname,,}
pkgver=6.0.0
pkgrel=1
pkgdesc='Gaussian Mixture Modelling for Model-Based Clustering, Classification, and Density Estimation'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
)
optdepends=(
  r-geometry
  r-knitr
  r-mass
  r-mix
  r-rmarkdown
)
makedepends=(
  gcc-fortran
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('de7c306ecba1ef0f4e4a56c748ce08149417496b711beefb032d561a4c28122a')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
