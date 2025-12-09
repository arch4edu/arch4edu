# Maintainer: Elio <ancibrothers@gmail.com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_cranname=diffobj
_cranver=0.3.6
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=2
pkgdesc="Diffs for R Objects"
arch=(i686 x86_64)
url="https://cran.r-project.org/package=${_cranname}"
license=(GPL2 GPL3)
depends=(
  "r>=3.1.0" 
  "r-crayon>=1.3.2"
)
optdepends=(
  "r-knitr" 
  "r-rmarkdown"
)

# It uses cloud.r-project.org instead of cran to make use of the CDN.
source=("https://cloud.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
b2sums=('f1dd3138845bf8617e98a07fe567f0a40e814113ccd2788f13af190423b809c751f3dc613854da78a4d151d4dc591bc1c1166f0d2a2f7eb06fdeaae9e76147da')

build() {
  mkdir -p "${srcdir}/build/"
  R CMD INSTALL ${_cranname}_${_cranver}.tar.gz -l "${srcdir}/build/"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${srcdir}/build/${_cranname}" "${pkgdir}/usr/lib/R/library"
  if [[ -f "${_cranname}/LICENSE" ]]; then
      install -Dm0644 "${_cranname}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
  fi
}
