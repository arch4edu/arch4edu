# Maintainer: Serene-Arc <https://aur.archlinux.org/account/serene-arc>

_cranname=lsoda
_cranver=1.2
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=1
pkgdesc="A 'C++' header library for using the 'libsoda-cxx' library with R."
arch=('any')
url="https://cran.r-project.org/package=${_cranname}"
license=('MIT')
depends=(
    r
    r-rcpp
)
makedepends=(gcc)
optdepends=(
    r-desolve
    r-microbenchmark
    r-rcpparmadillo
    r-rcppeigen
)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
sha256sums=('85b52abd1d5495c06adf93436c150445bcb3992a1eb6f9ae5848f5a2bb317ce5')

build() {
  R CMD INSTALL ${_cranname}_${_cranver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"

  cp -a --no-preserve=ownership "${_cranname}" "${pkgdir}/usr/lib/R/library"
}
