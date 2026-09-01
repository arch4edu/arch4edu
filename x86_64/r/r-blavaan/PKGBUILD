# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=blavaan
_pkgver=0.6-1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Bayesian Latent Variable Analysis"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-or-later')
depends=(
  r-bayesplot
  r-coda
  r-future
  r-future.apply
  r-generics
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
  onetbb
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
  r-posterior
  r-rjags
  r-runjags
  r-semtools
  r-tinytest
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('d3af71e727fb25f5d7aaece2a1c560d9')
b2sums=('36b1248af85fc95454ac2a94dc1dc1c593e52b5cc89bba60f872522e1221af456e6fb4704d3f338b0148b9964442343e6c3af2edc0d14071232e4e9efc6b9cc3')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
