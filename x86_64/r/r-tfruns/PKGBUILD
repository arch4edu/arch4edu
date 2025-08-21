# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=tfruns
_pkgver=1.5.4
pkgname=r-${_pkgname,,}
pkgver=1.5.4
pkgrel=1
pkgdesc="Training Run Tools for 'TensorFlow'"
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('Apache')
depends=(
  r
  r-base64enc
  r-config
  r-jsonlite
  r-magrittr
  r-reticulate
  r-rlang
  r-rstudioapi
  r-tidyselect
  r-whisker
  r-yaml
)
optdepends=(
  r-here
  r-knitr
  r-rmarkdown
  r-testthat
  r-withr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('dd22af08aaf1af42e2ba3fba372d91e2f83639a3d73dc464e72c55e26f2a31d2')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
