# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=ggrastr
_pkgver=1.0.2
pkgname=r-${_pkgname,,}
pkgver=1.0.2
pkgrel=1
pkgdesc="Rasterize Layers for 'ggplot2'"
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('MIT')
depends=(
  r
  r-cairo
  r-ggbeeswarm
  r-ggplot2
  r-png
  r-ragg
)
optdepends=(
  r-knitr
  r-maps
  r-rmarkdown
  r-sf
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('cb27406dca99cea6440adf6edb7eb53141b60322452f5a5d4409e36516ad20d1')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
  install -Dm644 "${_pkgname}/LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
