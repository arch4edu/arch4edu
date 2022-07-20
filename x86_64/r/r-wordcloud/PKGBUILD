# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=wordcloud
_pkgver=2.6
pkgname=r-${_pkgname,,}
pkgver=2.6
pkgrel=4
pkgdesc='Word Clouds'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('LGPL')
depends=(
  r
  r-rcolorbrewer
  r-rcpp
)
optdepends=(
  r-slam
  r-tm
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('53716954430acd4f164bfd8eacd7068a908ee3358293ded6cd992d53b7f72649')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
