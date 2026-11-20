# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=systemfonts
_pkgver=1.3.3
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="System Native Font Finding"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  fontconfig
  freetype2
  r-jsonlite
  r-lifecycle
  r-base64enc
)
makedepends=(
  r-cpp11
)
checkdepends=(
  r-testthat
  ttf-font
)
optdepends=(
  r-covr
  r-farver
  r-knitr
  r-rmarkdown
  r-testthat
  r-ggplot2
  r-ragg
  r-svglite

)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('db0e538d68e478ef0eaa970fe3f6411c')
b2sums=('579aa764265dbae8aed8384ed76ad08f51db57dc4584065e114e7bf4b5e16ab485c11da20035663fad7f917fcca460248d995c7ec38492863c7d5a0742dbdb12')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

check() {
  cd "$_pkgname/tests"
  R_LIBS="$srcdir/build" NOT_CRAN=true Rscript --vanilla testthat.R
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"

  install -d "$pkgdir/usr/share/licenses/$pkgname"
  ln -s "/usr/lib/R/library/$_pkgname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname"
}
