# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=LaplacesDemon
_pkgver=16.1.6
pkgname=r-${_pkgname,,}
pkgver=16.1.6
pkgrel=4
pkgdesc='Complete Environment for Bayesian Inference'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('MIT')
depends=(
  r
)
optdepends=(
  r-kernsmooth
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('57b53882fd7a195b38bbdbbf0b17745405eb3159b1b42f7f11ce80c78ab94eb7')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
  install -Dm644 "${_pkgname}/LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
