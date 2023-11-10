# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Robert Greener <me@r0bert.dev>
# Contributor: Thomas Ivesdal-Tronstad <thotro at lyse dot net>

_pkgname=pracma
_pkgver=2.4.4
pkgname=r-${_pkgname,,}
pkgver=2.4.4
pkgrel=1
pkgdesc='Practical Numerical Math Functions'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
)
optdepends=(
  r-nlcoptim
  r-quadprog
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('1a4ef3af2197f999dbaa614bf5a70f09ec463d8c91feb5aa0d995de24ec6ba7f')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
