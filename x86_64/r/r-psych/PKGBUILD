# Maintainer: Robert Greener <me@r0bert.dev>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: frichtlm <frichtlm@gmail.com>

_cranname=psych
_cranver=2.2.5
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=1
pkgdesc="Procedures for Psychological, Psychometric, and Personality Research"
arch=(any)
url="https://cran.r-project.org/package=${_cranname}"
license=(GPL2 GPL3)
depends=(r r-mnormt)
optdepends=(r-psychtools r-gparotation r-lavaan r-lme4 r-rcsdp r-graph r-knitr r-rgraphviz)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
sha512sums=('a804bad30bd08aa73ffc24c03d3c68fa8b60595a6ecc8b10e3652d0d7a71509943617b49ee038c7c618528f34333cb2bcbf6b88f6a783655c48aad87a0b05770')

build() {
  R CMD INSTALL ${_cranname}_${_cranver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"

  cp -a --no-preserve=ownership "${_cranname}" "${pkgdir}/usr/lib/R/library"
}
