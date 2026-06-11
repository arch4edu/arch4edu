# system requirements: C++11
# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=gridtext
_pkgver=0.1.6
pkgname=r-${_pkgname,,}
pkgver=0.1.6
pkgrel=1
pkgdesc="Improved Text Rendering Support for 'Grid' Graphics"
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('MIT')
depends=(
  r
  r-curl
  r-jpeg
  r-markdown
  r-png
  r-rcpp
  r-rlang
  r-stringr
  r-xml2
  gcc
)
optdepends=(
  r-covr
  r-knitr
  r-rmarkdown
  r-testthat
  r-vdiffr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('2b380e133719582e37cbb68754b0e0b009d95c7ad7e9d3da40d38dd858ee81de')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
  install -Dm644 "${_pkgname}/LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
