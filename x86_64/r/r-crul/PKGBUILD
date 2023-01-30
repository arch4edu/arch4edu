# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=crul
_pkgver=1.3
pkgname=r-${_pkgname,,}
pkgver=1.3
pkgrel=1
pkgdesc='HTTP Client'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('MIT')
depends=(
  r
  r-curl
  r-httpcode
  r-jsonlite
  r-mime
  r-r6
  r-urltools
)
optdepends=(
  r-fauxpas
  r-knitr
  r-rmarkdown
  r-roxygen2
  r-testthat
  r-webmockr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('8058617d8b3724acb5b89d0e6e63f381df5c56565128b250a65eceb2b8081e2d')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
  install -Dm644 "${_pkgname}/LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
