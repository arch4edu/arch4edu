# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Robert Greener <me@r0bert.dev>

_pkgname=biglm
_pkgver=0.9-3
pkgname=r-${_pkgname,,}
pkgver=0.9.3
pkgrel=1
pkgdesc='Bounded Memory Linear and Generalized Linear Models'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-dbi
)
optdepends=(
  r-leaps
  r-rodbc
  r-rsqlite
)
makedepends=(
  gcc-fortran
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('805d483dc58c041f1616267abeb39cecaaf7271a34e90668a5439383bf9a0d58')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
