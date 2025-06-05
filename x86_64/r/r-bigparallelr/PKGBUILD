# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=bigparallelr
_pkgver=0.3.2
pkgname=r-${_pkgname,,}
pkgver=0.3.2
pkgrel=4
pkgdesc='Easy Parallel Tools'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-bigassertr
  r-doparallel
  r-flock
  r-foreach
  r-parallelly
  r-rhpcblasctl
)
optdepends=(
  r-covr
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('5a3312699fdf6521e982b6fce844977dd7e9c3188354a7c3106c24495e643393')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
