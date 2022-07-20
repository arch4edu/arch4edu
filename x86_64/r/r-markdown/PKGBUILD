# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_cranname=markdown
_cranver=1.1
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=1
pkgdesc="Render Markdown with the C Library 'Sundown'"
arch=(i686 x86_64)
url="https://cran.r-project.org/package=${_cranname}"
license=(GPL2)
depends=('r>=2.11.1' r-xfun 'r-mime>=0.3')
optdepends=(r-knitr r-rcurl)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
sha256sums=('8d8cd47472a37362e615dbb8865c3780d7b7db694d59050e19312f126e5efc1b')

build() {
  R CMD INSTALL ${_cranname}_${_cranver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"

  cp -a --no-preserve=ownership "${_cranname}" "${pkgdir}/usr/lib/R/library"
}
