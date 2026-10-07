# Maintainer: AutoUpdateBot <auto_update_bot@arch4edu.org>

_pkgname=tidyplots
_pkgver=0.4.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Tidy plots for scientific papers"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  r
  r-cli
  r-dplyr
  r-forcats
  r-ggbeeswarm
  r-ggplot2
  r-ggpubr
  r-ggrastr
  r-ggrepel
  r-glue
  r-gtable
  r-hmisc
  r-htmltools
  r-lifecycle
  r-purrr
  r-rlang
  r-scales
  r-stringr
  r-tidyr
  r-tidyselect
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('41d353ac62899760fe6bf8138f7b0c3e')
b2sums=('a127b6a7a704418868be9158cfeb5eb3f7665d5e623aa1e4e5f9f36491fde74314889dd1757fe307fa5e1fe3963ec837d591cb8ecf2aad1e143c31959c65c37d')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"

  install -Dm644 "$_pkgname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
