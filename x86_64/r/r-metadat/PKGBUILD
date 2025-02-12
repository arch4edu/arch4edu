# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=metadat
_pkgver=1.4-0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Meta-Analysis Datasets"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r-mathjaxr
)
optdepends=(
  r-ape
  r-biasedurn
  r-clubsandwich
  r-dfoptim
  r-digest
  r-gridextra
  r-igraph
  r-lme4
  r-meta
  r-metafor
  r-mvtnorm
  r-netmeta
  r-numderiv
  r-rms
  r-testthat
  r-bayesmeta
  r-ellipse
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('adaa29e04468cc4d8619dfa008fec3cb')
b2sums=('841438693125131f394330030585464b9304ba5cc23a9f297c3fda4c321f0bdd0d569a4029fc544e374fbe4b97f4f992f2b3e6d2ea3339f565623bde5dd388fb')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
