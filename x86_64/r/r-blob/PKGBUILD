# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=blob
_pkgver=1.3.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="A Simple S3 Class for Representing Vectors of Binary Data ('BLOBS')"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  r-rlang
  r-vctrs
)
checkdepends=(
  r-testthat
)
optdepends=(
  r-covr
  r-crayon
  r-pillar
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('8a43f72d9dff0b574606a9d8b191c33a')
b2sums=('c2fd0941b0f145934d19d2a93c5df03538ec29e706c11125f0c75475cf15917538d32fc3dacae408aa29062aaf7573e87d358e9387839521c65229cd379adbd6')

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
