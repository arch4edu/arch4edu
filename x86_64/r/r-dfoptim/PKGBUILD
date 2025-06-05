# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=dfoptim
_pkgver=2023.1.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
pkgdesc="Derivative-Free Optimization"
arch=('any')
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r
)
optdepends=(
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('fa0cc871a9d611318ecf2e1f671f10a6')
b2sums=('3fc51d9fd8e63d71228ed3f708de15a5d3a32ccc9a4c631f219044516cd36f753b1f55df29e1cc878b5577f9534e01b20cd078006256feeced73f0b01e050bfe')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
