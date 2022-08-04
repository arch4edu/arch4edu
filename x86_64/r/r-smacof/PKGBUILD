# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=smacof
_pkgver=2.1-5
pkgname=r-${_pkgname,,}
pkgver=2.1.5
pkgrel=1
pkgdesc='Multidimensional Scaling'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-candisc
  r-colorspace
  r-doparallel
  r-e1071
  r-ellipse
  r-foreach
  r-hmisc
  r-nnls
  r-plotrix
  r-polynom
  r-weights
  r-wordcloud
)
optdepends=(
  r-calibrate
  r-ggplot2
  r-knitr
  r-mpsychor
  r-prefmod
  r-rmarkdown
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('fb0369a94bbdcb2b024d11731f2dda1a783b535aa243a00dd783a47a86192ac5')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
