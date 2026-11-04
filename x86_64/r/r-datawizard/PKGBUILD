# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=datawizard
_pkgver=1.5.0
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
  r-lmertest
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
md5sums=('be53b18207e1e6f6dcba8931f0c35c2f')
b2sums=('dcd3f3ffe82d31d0733365b3db28f688b7070e1f8cd48432eb63370df8fdb0cd29132dc6e8182bef2f6e80d9d5e8b4402be15ec9e0e9b90ddf8b90e453b1d389')

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
