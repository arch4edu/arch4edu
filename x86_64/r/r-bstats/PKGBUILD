#Maintainer: sukanka <su975853527 AT gmail.com>
_pkgname=bstats
_pkgver=0.0.0.9003
pkgname=r-${_pkgname,,}
pkgver=0.0.0.9003
pkgrel=1
pkgdesc="Bayesian statistics"
arch=('x86_64')
url="https://github.com/AlexanderLyNL/${_pkgname}"
license=('LGPL3')
depends=(r
 	  r-hypergeo
    r-purrr
    r-suppdists
)
makedepends=(git)
optdepends=()
source=("git+https://github.com/AlexanderLyNL/${_pkgname}.git")
sha256sums=('SKIP')


build() {
  mkdir -p ${srcdir}/usr/lib/R/library
  R -e "install.packages('${srcdir}/${_pkgname}',\
     type='source', repos=NULL,lib='${srcdir}/usr/lib/R/library', INSTALL_opts='--no-multiarch --no-docs --no-test-load')"
}

package() {
  cp -a --no-preserve=ownership "${srcdir}/usr" "${pkgdir}"
}
