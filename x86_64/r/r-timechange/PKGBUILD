# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=timechange
_pkgver=0.2.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
pkgdesc="Efficient Manipulation of Date-Times"
arch=(x86_64)
url="https://cran.r-project.org/package=${_pkgname}"
license=(GPL3)
depends=(
  cctz
  r
)
makedepends=(
  r-cpp11
)
checkdepends=(
  r-testthat
)
optdepends=(
  r-knitr
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz"
        "system-cctz.patch")
md5sums=('9e8dea7a23e233cccec70f7838381582'
         'a573af9ccae2bad5627178a50de35e5b')
sha256sums=('3d602008052123daef94a5c3f5154c5461b4ec0432ab70c37273d7ddd252f7f1'
            '77d128c19ede66d6f0a27d3751c15da2ac322bdf2ca0914d047ac36396156001')

prepare() {
  # build against system cctz
  patch -Np1 -i system-cctz.patch
}

build() {
  mkdir -p build
  R CMD INSTALL "$_pkgname" -l build
}

check() {
  cd "$_pkgname/tests"
  R_LIBS="$srcdir/build" NOT_CRAN=true Rscript --vanilla testthat.R
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}
