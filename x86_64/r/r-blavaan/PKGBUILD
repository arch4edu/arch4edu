# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=blavaan
_pkgver=0.5-10
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
  r-igraph
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
md5sums=('c22d52e0d54520ce498de60ddead2dc4')
b2sums=('d6ebdf09a37f42ec79f89819d5b138370848ecf35ac20518d36c443b371a1ca432ef5b1bc68ca357b0ed6afbd024b77f3a58dd90bc18ab2e1af6bcb598135740')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
