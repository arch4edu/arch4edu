# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=LaplacesDemon
_pkgver=16.1.6
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=8
pkgdesc="Complete Environment for Bayesian Inference"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('7b23b0c00987f6974aad4795ad7b6614')
b2sums=('8140b1bc034bf8d8f1ea8544200abdd715396bd9d92e5a6b73228d9c94859c82b4ef0eb54cb87fef26993116973827ee3a81d94b58c242e2d249a3983917b179')

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
