# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: sukanka <su975853527@gmail.com>

_pkgname=restriktor
_pkgver=0.5-30
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
pkgdesc="Restricted Statistical Estimation and Inference for Linear Models"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r-ggplot2
  r-ic.infer
  r-lavaan
  r-mvtnorm
  r-norm
  r-quadprog
)
optdepends=(
  r-bain
  r-knitr
  r-rmarkdown
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('ec3023fa71654bd421e7c1f82c1be9fc')
b2sums=('e9814dd03960af3f905d29eb96d47de8cdf2efd1d67ecdcff1e93e4e169d354faa5923409f180340c6ee3d0960a00bccbb240af039a727a884e487b9607b333e')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
