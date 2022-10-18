# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Robert Greener <me@r0bert.dev>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=TH.data
_pkgver=1.1-1
pkgname=r-${_pkgname,,}
pkgver=1.1.1
pkgrel=9
pkgdesc="TH's Data Archive"
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
)
optdepends=(
  r-atr
  r-coin
  r-colorspace
  r-dplyr
  r-gdata
  r-gridextra
  r-knitr
  r-lattice
  r-multcomp
  r-plyr
  r-rms
  r-tram
  r-trtf
  r-vcd
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('edf3ab16b142f4c52d21fc64e41409ed138e5b3e142f2fae964b00f02d53dd7a')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
