# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=mcmc
_pkgver=0.9-8
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
pkgdesc="Markov Chain Monte Carlo"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  r
)
optdepends=(
  r-iso
  r-xtable
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('429599a7f24105629c41dd7c9f36b992')
b2sums=('d804249a6244e3104687497c83472ec69411e05f3ce580d11b79b3a0278ed2c27d8b902ca6aa3d87f8da3ec169249ffb135ac99e4db17dc688e144e6b95912d7')

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
