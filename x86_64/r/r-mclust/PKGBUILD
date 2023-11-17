# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=mclust
_pkgver=6.0.1
pkgname=r-${_pkgname,,}
pkgver=6.0.1
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
sha256sums=('0e92de6fd1bd2a13de2c94eae84fba0d3762099a2505e05b887f1c2a7242537f')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
