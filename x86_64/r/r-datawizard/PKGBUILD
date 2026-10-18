# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=datawizard
_pkgver=1.4.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Easy Data Wrangling and Statistical Transformations"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  r-insight
)
optdepends=(
  r-bayestestr
  r-bh
  r-brms
  r-curl
  r-data.table
  r-discovr
  r-dplyr
  r-effectsize
  r-emmeans
  r-fixest
  r-gamm4
  r-ggplot2
  r-gt
  r-haven
  r-httr
  r-knitr
  r-lme4
  r-mediation
  r-modelbased
  r-nanoparquet
  r-openssl
  r-parameters
  r-performance
  r-poorman
  r-psych
  r-readr
  r-readxl
  r-rio
  r-rmarkdown
  r-rstanarm
  r-see
  r-testthat
  r-tibble
  r-tidyr
  r-tinytable
  r-withr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('ef3a3e726610cd14421c195bd19c035d')
b2sums=('ad0ab0a94c92a86a5345fbb2bb1c23f72a67fa72644eeb33ace1edb8b71f747cf112fd086dd559b3c2d5faa6e7dbcfa4dea5b8f4c431eb13ea7a4bf308a1663c')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"

  install -d "$pkgdir/usr/share/licenses/$pkgname"
  ln -s "/usr/lib/R/library/$_pkgname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname"
}
