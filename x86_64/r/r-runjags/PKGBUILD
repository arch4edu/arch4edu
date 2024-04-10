# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=runjags
_pkgver=2.2.2-4
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
pkgdesc="Interface Utilities, Model Templates, Parallel Computing Methods and Additional Distributions for MCMC Models in JAGS"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only')
depends=(
  jags
  r-coda
)
optdepends=(
  r-knitr
  r-markdown
  r-modeest
  r-rjags
  r-spelling
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('0c6bbf7794879f2a345929252d83041c')
b2sums=('787baaf661a16f97f27f721db8a7c7bf040798d53411c09a037b815149906d5f627c5af8b857eeb80f24540c33d2008970b3f426e3bfd7d88b647cc65d98e05a')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
