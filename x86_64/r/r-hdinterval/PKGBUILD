# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=HDInterval
_pkgver=0.2.4
pkgname=r-${_pkgname,,}
pkgver=0.2.4
pkgrel=1
pkgdesc='Highest (Posterior) Density Intervals'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
)
optdepends=(
  r-coda
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('bb07f0edd660a02ed18e578c2798eb8c2db0e181a5e0c3e23db182d13e9494f6')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
