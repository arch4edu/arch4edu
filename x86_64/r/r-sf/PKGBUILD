# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: peippo <christoph+aur@christophfink.com>

_pkgname=sf
_pkgver=1.0-21
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Simple Features for R"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only OR MIT')
depends=(
  gdal
  geos
  proj
  r-classint
  r-dbi
  r-magrittr
  r-s2
  r-units
)
makedepends=(
  r-rcpp
)
checkdepends=(
  postgis
  r-blob
  r-dplyr
  r-raster
  r-rpostgres
  r-rpostgresql
  r-sp
  r-testthat
  r-tidyr
)
optdepends=(
  r-blob
  r-covr
  r-dplyr
  r-ggplot2
  r-knitr
  r-lwgeom
  r-maps
  r-mapview
  r-microbenchmark
  r-nanoarrow
  r-odbc
  r-pbapply
  r-pillar
  r-pool
  r-raster
  r-rlang
  r-rmarkdown
  r-rpostgres
  r-rpostgresql
  r-rsqlite
  r-sp
  r-spatstat
  r-spatstat.geom
  r-spatstat.linnet
  r-spatstat.random
  r-spatstat.utils
  r-stars
  r-terra
  r-testthat
  r-tibble
  r-tidyr
  r-tidyselect
  r-tmap
  r-vctrs
  r-wk
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz"
        "fix-tests.patch")
md5sums=('c59ee67484070c71683b86bf04ed3947'
         '1f0ac4a99a8706821bc498b734be839f')
b2sums=('cc3dcb8f97a3f3e0861846faeca86b31fe3b4918ee48df87fb01b96717e9f8fe91eeab8677289c8795ea6d244ae0b94ae4d9ee860124231049fe47f9e00c901e'
        '988ca59b2da630b1c730865f95f4b2c1ce3a88ed67ce49823914ce50f3fe6972ae44a5cb28037cd043e753ec062ab9ec19a4f7f70c05042e010005afec20cb11')

prepare() {
  # skip failing tests
  patch -Np1 -i fix-tests.patch

  # use PGHOST variable in tests
  sed -e 's/host = "localhost",//' \
      -e 's/host=localhost //' \
      -i "$_pkgname/tests/testthat/test-postgis_RPostgres.R"
}

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

check() {
  cd "$_pkgname/tests"

  # create database for tests
  export PGDATA=db
  export PGHOST="$(pwd)/host"
  mkdir host
  initdb
  pg_ctl -o "-h '' -k ${PGHOST@Q}" start
  createdb postgis
  psql postgis -c "CREATE EXTENSION postgis;"
  createdb empty

  R_LIBS="$srcdir/build" NOT_CRAN=true Rscript --vanilla testthat.R

  # shut down test database
  pg_ctl stop
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"

  install -d "$pkgdir/usr/share/licenses/$pkgname"
  ln -s "/usr/lib/R/library/$_pkgname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname"
}
