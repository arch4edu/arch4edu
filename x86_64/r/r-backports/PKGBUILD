# Maintainer: Kristian Niemi <kristian.niemi@gmail.com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Matt Frichtl <frichtlm@gmail.com>
# Contributor: Grey Christoforo <first name at last name dot net>
_cranname=backports
_cranver=1.5.1
pkgname=r-${_cranname,,}
pkgver=${_cranver//-/.}
pkgrel=1
pkgdesc="Reimplementations of Functions Introduced Since R-3.0.0"
arch=(any)
url="https://cran.r-project.org/package=${_cranname}"
license=('GPL-2.0-only')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
b2sums=('6c37f1d6487c0ab7bb830f9ce87280019e5052d271ae1820b2278354c5995eafc37ff73b313313423ca998c8e668d7161f8758b84e960e6a78f8df72e54fc522')

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
