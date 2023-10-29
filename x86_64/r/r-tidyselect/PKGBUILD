# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: frichtlm <frichtlm@gmail.com>

_pkgname=tidyselect
_pkgver=1.2.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=4
pkgdesc="Select from a Set of Strings"
arch=(any)
url="https://cran.r-project.org/package=${_pkgname}"
license=(MIT)
depends=(
  r-cli
  r-glue
  r-lifecycle
  r-rlang
  r-vctrs
  r-withr
)
checkdepends=(
  r-stringr
  r-testthat
)
optdepends=(
  r-covr
  r-crayon
  r-dplyr
  r-knitr
  r-magrittr
  r-rmarkdown
  r-stringr
  r-testthat
  r-tibble
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('147069ee8d8bc42f63f253311f6c1806')
sha256sums=('538d26b727e37d618e2efd3b00836048f103112a03e6994bf07a02392e269e3b')

prepare() {
  cd "$_pkgname/tests/testthat"

  # skip outdated snapshot tests
  sed -i '/"eval_select() produces correct backtraces"/a\ \ skip("outdated snapshot")' \
      test-eval-select.R
  sed -i -e '/"all_of() and any_of() check their inputs"/a\ \ skip("outdated snapshot")' \
      -e '/"`all_of()` fails even if `.strict` is FALSE"/a\ \ skip("outdated snapshot")' \
      test-helpers-vector.R
  sed -i '/"where() checks return values"/a\ \ skip("outdated snapshot")' \
      test-helpers-where.R
  sed -i -e '/"vars_select() type-checks inputs"/a\ \ skip("outdated snapshot")' \
      -e '/"vars_rename() type-checks arguments"/a\ \ skip("outdated snapshot")' \
      test-lifecycle-deprecated.R
  sed -i -e '/"errors for bad inputs"/a\ \ skip("outdated snapshot")' \
      -e '/"vars_pull() produces correct backtraces"/a\ \ skip("outdated snapshot")' \
      test-vars-pull.R
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

  install -d "$pkgdir/usr/share/licenses/$pkgname"
  ln -s "/usr/lib/R/library/$_pkgname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname"
}
