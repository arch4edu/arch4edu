# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=fastmap
_pkgver=1.2.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
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
md5sums=('f53773acd6ba9a86413e8c2dc6441544'
         'bb23578b236de5d3de6a2fd2505814ba')
b2sums=('dff9cceb0859b47b182da062f7844ccfa703f077c92c1e1954681394c9cc8c2aca889bbd61220db4dcefb461834af0715128b3db2ddba6c853b41806b7d8c1d5'
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
