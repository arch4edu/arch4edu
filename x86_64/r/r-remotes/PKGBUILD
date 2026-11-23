# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=remotes
_pkgver=2.5.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=4
pkgdesc="R Package Installation from Remote Repositories, Including 'GitHub'"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  r
)
optdepends=(
  "git: alternative install_git backend"
  "subversion: install_svn"
  r-brew
  r-callr
  r-covr
  r-curl
  r-git2r
  r-knitr
  r-mockery
  r-pingr
  r-pkgbuild
  r-rmarkdown
  r-rprojroot
  r-testthat
  r-webfakes
  r-withr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('4cb0cd9d66630548fedd4e56d3564b90')
b2sums=('ee0959efb26f76e193c122797648bd1a52bc72154d5dce7707bc2198f7d79a9e33414157c6d964989709f4a06af3a429cbb74dc3b0c4c555861f11e0c5e3cc7c')

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
