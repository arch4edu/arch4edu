# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=LaplacesDemon
_pkgver=16.1.8
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Complete Environment for Bayesian Inference"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('f18ac0689624139efdb02e6a0c54ba53')
b2sums=('4e509752f253e1abd228302945a4a3b8e160c2bee3f352b2da9df2ee5aa7a063baa0e13174482c259868209704d255fc4dd92fe85d116d758878fdcc8d3091a2')

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
