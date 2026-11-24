# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=runjags
_pkgver=2.3.1-1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Interface Utilities, Model Templates, Parallel Computing Methods and Additional Distributions for MCMC Models in JAGS"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only')
depends=(
  jags
  r-coda
  r-rjags
)
optdepends=(
  r-knitr
  r-litedown
  r-markdown
  r-modeest
  r-spelling
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('3a6faa31d3cf99692faf9125975f76f1')
b2sums=('7ecb9f47d309a916fa4444dbf51a6cab6b73a774337c578df91c4b98d94940b6cca38ac5a1758fef54a0a02402a159b593e3df42c7befccaa19cf861516ea361')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
