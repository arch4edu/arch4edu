# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=Brobdingnag
_pkgver=1.2-7
pkgname=r-${_pkgname,,}
pkgver=1.2.7
pkgrel=5
pkgdesc='Very Large Numbers in R'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
)
optdepends=(
  r-cubature
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('73a734342736da5b29c2827d91f662101873503af7ad9cdf9e9e697bb32dd742')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
