# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=RPostgreSQL
_pkgver=0.7-8
pkgname=r-${_pkgname,,}
pkgver=0.7.8
pkgrel=1
pkgdesc="R Interface to the 'PostgreSQL' Database System"
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-dbi
  postgresql-libs
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('f215ab6ffe2533e56018f07cbb42014e1430b84bf56e9bd2cc8fd066e8f0963c')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
