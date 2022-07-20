# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=gridGraphics
_pkgver=0.5-1
pkgname=r-${_pkgname,,}
pkgver=0.5.1
pkgrel=4
pkgdesc="Redraw Base Graphics Using 'grid' Graphics"
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
)
optdepends=(
  r-magick
  r-pdftools
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('29086e94e63891884c933b186b35511aac2a2f9c56967a72e4050e2980e7da8b')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
