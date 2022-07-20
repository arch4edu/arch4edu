# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=fdrtool
_pkgver=1.2.17
pkgname=r-${_pkgname,,}
pkgver=1.2.17
pkgrel=4
pkgdesc='Estimation of (Local) False Discovery Rates and Higher Criticism'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('3452601adbead9be4820794e3af2666f710fdf9b801186df565b80b43629c5dd')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
