# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Robert Greener <me@r0bert.dev>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: frichtlm <frichtlm@gmail.com>

_pkgname=psych
_pkgver=2.6.9
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Procedures for Psychological, Psychometric, and Personality Research"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r-gparotation
  r-mnormt
)
optdepends=(
  r-graph
  r-knitr
  r-lavaan
  r-lme4
  r-psychtools
  r-rcsdp
  r-rgraphviz
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('843724d4f8e8dc92cf63b80d869c3320')
b2sums=('56051edd7a15ebb81c4de1f276c893972cf6b879ad96abda3dfb11d4719b43d831e1aa0ac4e61c56a9a7e4bb11a7159256f1ac6398dea48922cd257493d8c6c0')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
