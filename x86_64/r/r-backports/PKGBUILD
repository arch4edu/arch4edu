# Maintainer: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Matt Frichtl <frichtlm@gmail.com>
# Contributor: Grey Christoforo <first name at last name dot net>

_cranname=backports
_cranver=1.5.0
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=1
pkgdesc="Reimplementations of Functions Introduced Since R-3.0.0"
arch=(i686 x86_64)
url="https://cran.r-project.org/package=${_cranname}"
license=("GPL-2.0-only" "GPL-3.0-only")
depends=("r>=3.0.0")
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
b2sums=("682625e314e7574a9eff14601ef70793c2916639c6a28443472be172d3099c03f63b550353546e7dc88667ad9605e38f195ca97e68e6d21bad399993488c25ce")

build() {
  R CMD INSTALL ${_cranname}_${_cranver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"

  cp -a --no-preserve=ownership "${_cranname}" "${pkgdir}/usr/lib/R/library"
}
