# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=ggraph
_pkgver=2.2.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="An Implementation of Grammar of Graphics for Graphs and Networks"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  r-cli
  r-dplyr
  r-ggforce
  r-ggplot2
  r-ggrepel
  r-graphlayouts
  r-igraph
  r-lifecycle
  r-memoise
  r-rlang
  r-scales
  r-tidygraph
  r-vctrs
  r-viridis
  r-withr
)
makedepends=(
  r-cpp11
)
optdepends=(
  r-covr
  r-deldir
  r-gganimate
  r-knitr
  r-network
  r-purrr
  r-rmarkdown
  r-seriation
  r-sf
  r-sfnetworks
  r-tibble
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('cacb7920286e8197ea44a31749319981')
b2sums=('cc6566fc1558d2d1091117624f2198f20a2872eb2a68698b5ca7ee0f99dfc1f7b0800fcbfe542d1dad676b02e70c9d47f7d5f335154d97a88c1c515b1e0534a8')

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
