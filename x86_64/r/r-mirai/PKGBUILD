# Maintainer: Jingbei Li <i@jingbei.li>
_cranname=mirai
_pkgver=2.7.2
pkgname=r-mirai
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Minimalist Async Evaluation Framework for R"
arch=(x86_64)
url="https://cran.r-project.org/package=${_cranname}"
license=(MIT + file LICENSE)
depends=(r r-nanonext)
makedepends=(gcc-fortran)
optdepends=(r-cli r-litedown r-mori r-otel r-otelsdk r-secretbase)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_pkgver}.tar.gz")

build() {
  R CMD INSTALL ${_cranname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_cranname}" "${pkgdir}/usr/lib/R/library"
  install -Dm644 "${_cranname}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
sha256sums=('78a32dac63fbc4da00aaa8c4c15d6c2d8b41bb1addf88a0bdaf96add58fb5939')
