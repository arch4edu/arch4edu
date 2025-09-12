# system requirements: git (optional)
# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=credentials
_pkgver=2.0.3
pkgname=r-${_pkgname,,}
pkgver=2.0.3
pkgrel=1
pkgdesc='Tools for Managing SSH and Git Credentials'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('MIT')
depends=(
  r
  r-askpass
  r-curl
  r-jsonlite
  r-openssl
  r-sys
)
optdepends=(
  git
  r-knitr
  r-rmarkdown
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('140043804b4cfcb5e174af3a188ce4cd1e17f7f6aeb777bbd4da21f6c73e013c')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
  install -Dm644 "${_pkgname}/LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
