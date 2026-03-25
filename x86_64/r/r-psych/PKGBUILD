# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Robert Greener <me@r0bert.dev>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: frichtlm <frichtlm@gmail.com>

_pkgname=psych
_pkgver=2.6.3
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
md5sums=('21b5a90169b4ae83cf898401e519fbc3')
b2sums=('8c9d4add05977a15c9bd4756ff9d93970348430cea9a535f9af87d6a6557cede8e94cd8661daa1f092b7bf7196d5314b22f6dad1fe8c295ac2840e994ad11259')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
