# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Grey Christoforo <first name at last name dot net>

_cranname=RColorBrewer
_cranver=1.1-3
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=1
pkgdesc="ColorBrewer Palettes"
arch=(any)
url="https://cran.r-project.org/package=${_cranname}"
license=(Apache2.0)
depends=('r>=2.0.0')
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
sha256sums=("4f42f5423c45688b39f492c7892d93f37b4541831c8ffb140364d2bd89031ac0")

build() {
  R CMD INSTALL ${_cranname}_${_cranver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_cranname}" "${pkgdir}/usr/lib/R/library"

  if [[ -f "${_cranname}/LICENSE" ]]; then
    install -Dm0644 "${_cranname}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
  fi

}
