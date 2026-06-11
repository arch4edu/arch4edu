# Maintainer: Kristian Niemi <kristian.niemi@gmail.com>
# Contributor: peippo <christoph+aur@christophfink.com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Grey Christoforo <first name at last name dot net>
_cranname=viridisLite
_cranver=0.4.3
pkgname=r-${_cranname,,}
pkgver=${_cranver//-/.}
pkgrel=1
pkgdesc="Colorblind-Friendly Color Maps (Lite Version)"
arch=(any)
url="https://cran.r-project.org/package=${_cranname}"
license=('MIT')
depends=(
  r
)
optdepends=(
  r-hexbin
  r-ggplot2
  r-testthat
  r-covr
)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
b2sums=('88fbefc57987361a5c8ed1488b081de93d01a70a27358c612ec1e554d6f66b321686db160d09b1868ca3e3e694710cc80c0082485a6b260c9b1961280d289a3c')

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
