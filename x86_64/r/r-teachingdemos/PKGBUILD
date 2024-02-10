# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=TeachingDemos
_pkgver=2.12.1
pkgname=r-${_pkgname,,}
pkgver=2.12.1
pkgrel=1
pkgdesc='Demonstrations for Teaching and Learning'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('Artistic2.0')
depends=(
  r
)
optdepends=(
  r-ggplot2
  r-lattice
  r-logspline
  r-manipulate
  r-maptools
  r-mass
  r-png
  r-r2wd
  r-rgl
  r-tcltk
  r-tcltk2
  r-tkrplot
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('f5b189c767b76594808ae678b7e4b1e0e6bf0cee80c70df9e41edfb81aaaf3a8')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
