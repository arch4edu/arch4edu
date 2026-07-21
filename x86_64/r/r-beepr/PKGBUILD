# Maintainer: Jingbei Li <i@jingbei.li>
_cranname=beepr
pkgname=r-beepr
pkgver=2.0
pkgrel=1
pkgdesc="Easily Play Notification Sounds on any Platform"
arch=(x86_64)
url="https://cran.r-project.org/package=${_cranname}"
license=(GPLv3)
depends=(r r-audio)
makedepends=(gcc-fortran)
optdepends=(r-testthat)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${pkgver}.tar.gz")

build() {
  R CMD INSTALL ${_cranname}_${pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_cranname}" "${pkgdir}/usr/lib/R/library"
}

sha256sums=('620e5ec93c1a0991a9c8f60868153fee1e3918b1a784f50c0e35186780c60477')
