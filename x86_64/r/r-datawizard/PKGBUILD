# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=datawizard
_pkgver=1.4.0
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
md5sums=('b272c8962d793d156320c9a75cd14bd6')
b2sums=('85f7b1f26a5243b021619afab81edae349187b40a460018aeef0b4ee5d1aecd0c8c5fcb39791fb470c31aa4012e97a7a400d726e384cdbfe02adae2f2b13cb07')

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
