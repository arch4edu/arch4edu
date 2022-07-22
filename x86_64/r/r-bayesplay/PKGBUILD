# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=bayesplay
_pkgver=0.9.2
pkgname=r-${_pkgname,,}
pkgver=0.9.2
pkgrel=4
pkgdesc='The Bayes Factor Playground'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('MIT')
depends=(
  r
  r-gginnards
)
optdepends=(
  r-covr
  r-ggplot2
  r-knitr
  r-markdown
  r-rmarkdown
  r-testthat
  r-vdiffr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('5b134b10c3e702b427f4a40470d21d08cc33f73c83ae324c06d788658632211a')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
  install -Dm644 "${_pkgname}/LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
