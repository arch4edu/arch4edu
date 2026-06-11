# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=blavaan
_pkgver=0.5-8
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Bayesian Latent Variable Analysis"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-or-later')
depends=(
  onetbb
  r-bayesplot
  r-coda
  r-future.apply
  r-lavaan
  r-loo
  r-mnormt
  r-nonnest2
  r-rcpp
  r-rcppparallel
  r-rstan
  r-rstantools
  r-tmvnsim
)
makedepends=(
  r-bh
  r-rcppeigen
  r-stanheaders
)
optdepends=(
  r-blavsam
  r-cmdstanr
  r-modeest
  r-rjags
  r-runjags
  r-semtools
  r-tinytest
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('eae8d16d00892c002e61ce7fad35f5a5')
b2sums=('3c7c785c1137da7546d2a391b26decdc2ba4092039d09a5a712934b89214c197ad92ed13f545cb78ecaa8d528fc135d579e1b7604894f79a1745f08797873dbe')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
