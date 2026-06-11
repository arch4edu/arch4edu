# Maintainer: Kristian Niemi <kristian.niemi@gmail.com>
# Contributor: peippo <christoph+aur@christophfink.com>
# Contributor: Grey Christoforo <first name at last name dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Matt Frichtl <frichtlm@gmail.com>
# Contributor: wagnerflo <florian@wagner-flo.net>
_cranname=lazyeval
_cranver=0.2.3
pkgname=r-${_cranname,,}
pkgver=${_cranver//-/.}
pkgrel=1
pkgdesc="Lazy (Non-Standard) Evaluation"
arch=(any)
url="https://cran.r-project.org/package=${_cranname}"
license=('GPL-3.0-only')
depends=(
  r
  r-rlang
)
optdepends=(
  r-knitr
  r-rmarkdown
  r-testthat
  r-covr
)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
b2sums=('68fc5fee96f2aaf896f6e9e1c706aa36ba5313599a1c3d6feb75718e87ef45dd104c0d7df4c956a38d8235148a5f6f052f8b0b2e9691612f8231dbb5443398e3')

build() {
  mkdir -p "${srcdir}/build"
  R CMD INSTALL "${_cranname}_${_cranver}.tar.gz" -l "${srcdir}/build"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${srcdir}/build/${_cranname}" "${pkgdir}/usr/lib/R/library"
  if [[ -f "${srcdir}/build/${_cranname}/LICENSE" ]]; then
    install -Dm0644 "${srcdir}/build/${_cranname}/LICENSE" \
      "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
  fi
}
