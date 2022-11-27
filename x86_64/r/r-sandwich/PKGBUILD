# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Robert Greener <me@r0bert.dev>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=sandwich
_pkgver=3.0-2
pkgname=r-${_pkgname,,}
pkgver=3.0.2
pkgrel=6
pkgdesc='Robust Covariance Matrix Estimators'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-zoo
)
optdepends=(
  r-aer
  r-car
  r-geepack
  r-lattice
  r-lme4
  r-lmtest
  r-mass
  r-multiwayvcov
  r-parallel
  r-pcse
  r-plm
  r-pscl
  r-scatterplot3d
  r-stats4
  r-strucchange
  r-survival
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('6e30b6b554eb19430a60c45a8132fb7918ddb0013577bf6a62caeb163bdfe2b4')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
