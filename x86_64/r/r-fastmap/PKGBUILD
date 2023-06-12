# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=fastmap
_pkgver=1.1.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//[:-]/.}
pkgrel=4
pkgdesc="Fast Data Structures"
arch=(x86_64)
url="https://cran.r-project.org/package=${_pkgname}"
license=(MIT)
depends=(
  r
)
makedepends=(
  hopscotch-map
)
checkdepends=(
  r-testthat
)
optdepends=(
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz"
        "system-hopscotch-map.patch")
md5sums=('57a70be74ce88c5dc7e97c5547526f9f'
         'bb23578b236de5d3de6a2fd2505814ba')
sha256sums=('3623809dd016ae8abd235200ba7834effc4b916915a059deb76044137c5c7173'
            'a189963fc1d1c913df21bc02d0ba17678965d628775c03d39c2ffb6d4624680d')

prepare() {
  # Use system hopscotch_map
  patch -Np1 -i system-hopscotch-map.patch
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
