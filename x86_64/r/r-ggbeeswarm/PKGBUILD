# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=ggbeeswarm
_pkgver=0.7.3
pkgname=r-${_pkgname,,}
pkgver=0.7.3
pkgrel=1
pkgdesc='Categorical Scatter (Violin Point) Plots'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-beeswarm
  r-cli
  r-ggplot2
  r-lifecycle
  r-vipor
)
optdepends=(
  r-gridextra
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('5834381e53e38343e5720cf02a2b5be330ab440c1ac6d06e5dd62e59487c7060')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
