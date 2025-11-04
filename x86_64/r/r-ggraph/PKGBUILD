# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=ggraph
_pkgver=2.2.2
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
md5sums=('3e28dbb4cecc49ccfa1dd8de12e3af11')
b2sums=('781a6a8ba312e40299871fa11c1c7d9978f7c4908f7832a679c4ffbcdd033227ef2329bac8d5a3b8e14b94fcf9590c57e42019a25f386073302db9672037b2e8')

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
