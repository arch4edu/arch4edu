# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: sukanka <su975853527@gmail.com>

_pkgname=restriktor
_pkgver=0.5-80
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Restricted Statistical Estimation and Inference for Linear Models"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r-ggplot2
  r-glue
  r-gridextra
  r-ic.infer
  r-lavaan
  r-mvtnorm
  r-norm
  r-pbapply
  r-quadprog
  r-scales
  r-tmvtnorm
)
optdepends=(
  r-bain
  r-knitr
  r-rmarkdown
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('bcf4e810f04352d2f393c00cf2df421d')
b2sums=('e8066d3683fdbcacf164423e409444cad20021408afebe001247da334bdf35cc0b00856da7011f6f4e9f740fa59bb07fa27a3e2735912995f601ab799bdd3f3d')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
