# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Robert Greener <me@r0bert.dev>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: frichtlm <frichtlm@gmail.com>

_pkgname=psych
_pkgver=2.3.3
pkgname=r-${_pkgname,,}
pkgver=2.3.3
pkgrel=1
pkgdesc='Procedures for Psychological, Psychometric, and Personality Research'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-mnormt
)
optdepends=(
  r-gparotation
  r-graph
  r-knitr
  r-lavaan
  r-lme4
  r-psychtools
  r-rcsdp
  r-rgraphviz
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('94a9f3c39f8243573752709b89eb8068e11dbe809f86ecf0225fb429556efb6f')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:
