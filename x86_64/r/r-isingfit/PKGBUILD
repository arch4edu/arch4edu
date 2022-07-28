# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=IsingFit
_pkgver=0.3.1
pkgname=r-${_pkgname,,}
pkgver=0.3.1
pkgrel=1
pkgdesc='Fitting Ising Models Using the ELasso Method'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-glmnet
  r-qgraph
)
optdepends=(
  r-isingsampler
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('8741d65b63818c927819155f13a62d21f7d7f4942b9d218e6f93ce12eeff2ddf')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
