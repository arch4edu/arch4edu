# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=datawizard
_pkgver=1.3.0
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
  r-dplyr
  r-effectsize
  r-emmeans
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
  r-withr
  r-tinytable
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('e46be1e38941442afbe791f03d1db3fe')
b2sums=('743f939aa641f98b0de0995e812ccec74c445f560de1b2006771027b28d0c7dd4c0e1aea04a5a5784058a62fcc9683ad32fb559eb8800362af7fec38d1195276')

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
