# Maintainer: Serene-Arc <https://aur.archlinux.org/account/serene-arc>

_cranname=otel
_cranver=0.2.0
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=1
pkgdesc="High-quality, ubiquitous, and portable telemetry to enable effective observability."
arch=('any')
url="https://cran.r-project.org/package=${_cranname}"
license=('GPL3')
depends=(
    r
)
makedepends=()
optdepends=(
    r-callr
    r-cli
    r-glue
    r-jsonlite
    r-otelsdk
    r-processx
    r-shiny
    r-spelling
    r-testthat
    r-utils
    r-withr
)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
sha256sums=('ef8afe5a1bc8074bbeb8a84134699ef348a1f8ac629ffba25ee43ea7bcd8dd17')

build() {
  R CMD INSTALL ${_cranname}_${_cranver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"

  cp -a --no-preserve=ownership "${_cranname}" "${pkgdir}/usr/lib/R/library"
}
