# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=runjags
_pkgver=2.2.2-5
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
md5sums=('3bc563e2c68a78b6933a2a73acb62602')
b2sums=('c18a7a8eada0a3668db9db2edb5f36307c0de644627eb62e52e3243c77c633fb22c125fdfb0000c1e5ffe82c929e44a540ee3e86fccd94685a747a312189dc37')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
