# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=relimp
_pkgver=1.0-5
pkgname=r-${_pkgname,,}
pkgver=1.0.5
pkgrel=4
pkgdesc='Relative Contribution of Effects in a Regression Model'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
)
optdepends=(
  r-mass
  r-nnet
  r-rcmdr
  r-tcltk
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('acac7cf72ea39916761b51c825db0ffcb2bb1640e0a04086831fb78e9e40b679')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
