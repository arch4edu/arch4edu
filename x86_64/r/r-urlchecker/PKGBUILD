# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=urlchecker
_pkgver=1.0.1
pkgname=r-${_pkgname,,}
pkgver=1.0.1
pkgrel=1
pkgdesc='Run CRAN URL Checks from Older R Versions'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-cli
  r-curl
  r-xml2
)
optdepends=(
  r-covr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('62165ddbe1b748b58c71a50c8f07fdde6f3d19a7b39787b9fa2b4f9216250318')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
