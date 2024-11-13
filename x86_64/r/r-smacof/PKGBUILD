# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=smacof
_pkgver=2.1-7
pkgname=r-${_pkgname,,}
pkgver=2.1.7
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
sha256sums=('7a965a4e06a2ef1e01e37ae7ce6a55f2e745d4aaf99eb1c592b3d835bac9493a')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
