# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=fastmap
_pkgver=1.1.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=6
pkgdesc="Fast Data Structures"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
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
b2sums=('764fff53679057bddeccbf64e964479d884f870d726b315694b2a6525e3c5a98ff74c60535be79a847bcee01eb730d18878a7a06a93a53d599794fb5b6fb3703'
        'c8b327935db8add02be58fba70f99fc71b83322b293c9284897cbf34a5f31cb3151e3268f99088380528cbd53fd35b3d873bc8707ff3dac36ef382412722b82e')

prepare() {
  # Use system hopscotch_map
  patch -Np1 -i system-hopscotch-map.patch
}

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
