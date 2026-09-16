# Maintainer: Elio <ancibrothers@gmail.com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=diffobj
_pkgver=0.3.9
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=5
pkgdesc="Diffs for R Objects"
arch=(i686 x86_64)
url="https://cran.r-project.org/package=${_pkgname}"
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
source=("https://cloud.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
b2sums=('3b06abbaa178c1724b7030722a533d6cc525a58526e3c9ccf270f4e59cdf79c78352b9c3e32a4afab8da666522edcd622d6e236ad3a7975cc578314bc9f0a6b8')

build() {
  mkdir -p "${srcdir}/build/"
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}/build/"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${srcdir}/build/${_pkgname}" "${pkgdir}/usr/lib/R/library"
  if [[ -f "${_pkgname}/LICENSE" ]]; then
      install -Dm0644 "${_pkgname}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
  fi
}
