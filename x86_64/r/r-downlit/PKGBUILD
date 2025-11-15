# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=downlit
_pkgver=0.4.5
pkgname=r-${_pkgname,,}
pkgver=0.4.5
pkgrel=1
pkgdesc='Syntax Highlighting and Automatic Linking'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('MIT')
depends=(
  r
  r-brio
  r-desc
  r-digest
  r-evaluate
  r-fansi
  r-memoise
  r-rlang
  r-vctrs
  r-withr
  r-yaml
)
optdepends=(
  r-covr
  r-htmltools
  r-jsonlite
  r-mass
  r-massspecwavelet
  r-pkgload
  r-rmarkdown
  r-testthat
  r-xml2
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('b696ce388a804738b44eb1ceb0e3f0531b309ea91408f40a0cb43c63541b658b')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
  install -Dm644 "${_pkgname}/LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
